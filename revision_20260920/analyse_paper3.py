"""Rebuild Paper3 from source records and historical PBFs; aggregate outputs only."""
from pathlib import Path
import sys, json, hashlib, platform, argparse
P=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--clean-survey', type=Path, required=True, help='Restricted cleaned resident XLSX')
parser.add_argument('--raw-survey', type=Path, required=True, help='Restricted original resident response XLSX')
parser.add_argument('--pbf-dir', type=Path, required=True, help='Directory containing vietnam-230101.osm.pbf and vietnam-260101.osm.pbf')
parser.add_argument('--output-dir', type=Path, default=P/'analysis')
parser.add_argument('--cache-dir', type=Path, default=P/'restricted_cache')
parser.add_argument('--make-maps', action='store_true', help='Build disclosure-controlled study map and synthetic routing illustration')
parser.add_argument('--context-dir', type=Path, default=P/'context')
args=parser.parse_args()
for source in [args.clean_survey,args.raw_survey]+[args.pbf_dir/f'vietnam-{y}0101.osm.pbf' for y in ['23','26']]:
    if not source.is_file(): parser.error(f'Missing input: {source}')
import numpy as np, pandas as pd, osmium, networkx as nx
from pyproj import Transformer
from scipy.spatial import cKDTree
from scipy import stats
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=args.output_dir; OUT.mkdir(parents=True,exist_ok=True)
CACHE=args.cache_dir; CACHE.mkdir(parents=True,exist_ok=True)
TR=Transformer.from_crs(4326,32648,always_xy=True)
W,E,S,N=106.66,106.85,10.74,10.92
def xy(lon,lat): return np.column_stack(TR.transform(lon,lat))
def dump(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=lambda x: int(x) if isinstance(x,np.integer) else float(x)),encoding='utf-8')

class Nodes(osmium.SimpleHandler):
    def __init__(self): super().__init__(); self.coords={}; self.stops=[]
    def node(self,n):
        x,y=n.location.lon,n.location.lat
        if not (W<=x<=E and S<=y<=N): return
        self.coords[n.id]=(x,y); t=dict(n.tags)
        if t.get('highway')=='bus_stop' or t.get('bus')=='yes' or t.get('amenity')=='bus_station':
            self.stops.append({'id':'n'+str(n.id),'lon':x,'lat':y,'tags':t})
class Ways(osmium.SimpleHandler):
    def __init__(self,coords): super().__init__(); self.coords=coords; self.roads=[]; self.stops=[]
    def way(self,w):
        t=dict(w.tags); hw=t.get('highway')
        if not hw and not (t.get('bus')=='yes' or t.get('amenity')=='bus_station'): return
        ids=[n.ref for n in w.nodes]
        if not all(i in self.coords for i in ids): return
        coords=[self.coords[i] for i in ids]
        if hw: self.roads.append({'id':w.id,'ids':ids,'coords':coords,'tags':t})
        if t.get('bus')=='yes' or t.get('amenity')=='bus_station':
            a=np.array(coords); self.stops.append({'id':'w'+str(w.id),'lon':float(a[:,0].mean()),'lat':float(a[:,1].mean()),'tags':t})
def extract(year):
    cache=CACHE/f'osm_{year}.json'
    f=args.pbf_dir/f'vietnam-{str(year)[2:]}0101.osm.pbf'
    if cache.exists():
        cached=json.loads(cache.read_text(encoding='utf-8'))
        assert cached['pbf_sha256']==hashlib.sha256(f.read_bytes()).hexdigest(), 'PBF changed; rebuild its cache before proceeding'
        return cached
    a=Nodes(); a.apply_file(str(f)); b=Ways(a.coords); b.apply_file(str(f))
    obj={'stops':a.stops+b.stops,'roads':b.roads,'pbf_sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
    cache.write_text(json.dumps(obj,ensure_ascii=False),encoding='utf-8'); print('extracted',year,len(obj['stops']),len(obj['roads']),flush=True)
    return obj
def active(t):
    bus_feature = t.get('highway')=='bus_stop' or t.get('amenity')=='bus_station' or (t.get('bus')=='yes' and t.get('public_transport') in ['platform','station','stop_position'])
    return bus_feature and not (t.get('bus')=='no' or t.get('railway') in ['station','halt','stop','proposed','construction'] or any(t.get(k) in ['yes','bus_stop','platform','station'] for k in ['disused','abandoned','construction','proposed']) or t.get('access') in ['private','no'])
def stops(obj,strict=False):
    s=[r for r in obj['stops'] if active(r['tags']) and (r['tags'].get('highway')=='bus_stop' if strict else True)]
    df=pd.DataFrame(s); df['x'],df['y']=TR.transform(df.lon.values,df.lat.values)
    return df.drop_duplicates(['lon','lat']).reset_index(drop=True)
WALK={'footway','path','pedestrian','steps','track','residential','living_street','service','unclassified','tertiary','secondary','primary','road','tertiary_link','secondary_link','primary_link'}
def graph(obj):
    G=nx.Graph(); removed=0
    for w in obj['roads']:
        t=w['tags']; hw=t.get('highway'); foot=t.get('foot')
        if hw not in WALK and not(hw=='cycleway' and foot in ['yes','designated','permissive']): continue
        if foot in ['no','private'] or (t.get('access') in ['no','private'] and foot not in ['yes','designated','permissive']): removed+=1; continue
        a=np.array(w['coords']); ps=xy(a[:,0],a[:,1])
        for i in range(len(ps)-1):
            u,v=w['ids'][i:i+2]; dist=float(np.linalg.norm(ps[i+1]-ps[i]))
            if u==v: continue
            for j,node in [(i,u),(i+1,v)]: G.add_node(node,x=float(ps[j,0]),y=float(ps[j,1]))
            if not G.has_edge(u,v) or G[u][v]['weight']>dist: G.add_edge(u,v,weight=dist)
    return G,removed
def route(G,st,locs,maxsnap):
    ids=list(G); pos=np.array([[G.nodes[i]['x'],G.nodes[i]['y']] for i in ids]); tree=cKDTree(pos)
    ds,si=tree.query(st[['x','y']].values); dh,hi=tree.query(locs)
    H=G.copy(); source=-1; H.add_node(source)
    for dd,j in zip(ds,si):
        if dd>maxsnap: continue
        node=ids[j]
        if not H.has_edge(source,node) or H[source][node]['weight']>dd: H.add_edge(source,node,weight=float(dd))
    D=nx.single_source_dijkstra_path_length(H,source,weight='weight')
    out=np.array([D.get(ids[j],np.nan)+dd if dd<=maxsnap else np.nan for dd,j in zip(dh,hi)])
    return out,{'stops_snapped':int((ds<=maxsnap).sum()),'households_snapped':int((dh<=maxsnap).sum()),'routable':int(np.isfinite(out).sum()),'household_connector_median':float(np.median(dh)),'household_connector_max':float(np.max(dh))}

cit=pd.read_excel(args.clean_survey)
raw=pd.read_excel(args.raw_survey)
raw=raw.set_index('Timestamp'); cit['verified']=cit.Timestamp.isin(raw.index)
assert raw.index.is_unique and cit.Timestamp.is_unique, 'Timestamp linkage must be one-to-one'
matches=cit.loc[cit.verified].copy()
checks={}
for clean,prefix in [('Q1.10_PTDiChuyen','Q1.10 '),('Q2.8_LyDo_KSD_PTCC','Q2.8 '),('Q1.9_ThuNhapHoGD','Q1.9 '),('Q1.8_TrinhDo','Q1.8 ')]:
    rc=next(c for c in raw.columns if c.startswith(prefix))
    a=matches[clean].astype(str).str.strip().values; b=raw.loc[matches.Timestamp,rc].astype(str).str.strip().values
    checks[clean]={'matched':int((a==b).sum()),'different':int((a!=b).sum())}
    if clean in ['Q1.10_PTDiChuyen','Q2.8_LyDo_KSD_PTCC'] and np.any(a!=b):
        # Prefer raw response text for the source-verified cohort; retain clean as an audit field.
        cit.loc[cit.verified,clean]=raw.loc[matches.Timestamp,rc].values
reasonmap={'Thói quen sử dụng xe máy để di chuyển':'Motorcycle habit','Không cảm thấy thoải mái khi phải đi bộ đến các trạm':'Walking discomfort','Số lượng điểm dừng và tần suất các chuyến chưa đủ':'Stops and frequency','Thiếu cơ sở hạ tầng giữ xe cá nhân tại các trạm giao thông công cộng':'Parking at stops','Chất lượng xe buýt và thái độ phục vụ chưa tốt':'Bus quality and staff','Có sử dụng phương tiện công cộng':'Reports using public transport'}
cit['reason']=cit['Q2.8_LyDo_KSD_PTCC'].astype(str).str.strip().map(reasonmap)
assert cit.reason.notna().all(),cit.loc[cit.reason.isna(),'Q2.8_LyDo_KSD_PTCC'].unique()
cit['geo']=cit.Long.between(W,E)&cit.Lat.between(S,N)
cit['age']=2023-pd.to_numeric(cit.NamSinh,errors='coerce'); cit['female']=(cit.GioiTinh=='Nữ').astype(int)
cit['income']=cit['Q1.9_ThuNhapHoGD'].map({'<5 triệu/tháng':'Low','5-15 triệu/tháng':'Middle','15-25 triệu/tháng':'High','25-35 Triệu/tháng':'High','>35 Triệu/tháng':'High'})
cit['ward']=cit['Q1.2_DCTT_Phuong']; cit['walk']=(cit.reason=='Walking discomfort').astype(int); cit['habit']=(cit.reason=='Motorcycle habit').astype(int)
gidx=cit.index[cit.geo]; locations=xy(cit.loc[gidx,'Long'].values,cit.loc[gidx,'Lat'].values)
cit.loc[gidx,'block']=[f'{int(x//500)}_{int(y//500)}' for x,y in locations]
audit={}
for year in [2023,2026]:
    obj=extract(year); st=stops(obj); strict=stops(obj,True)
    for label,s in [('inclusive',st),('highway',strict)]:
        cit.loc[gidx,f'd_{label}_{year}']=cKDTree(s[['x','y']].values).query(locations)[0]
    pairs=cKDTree(st[['x','y']].values).query_pairs(50); dg=nx.Graph(); dg.add_nodes_from(range(len(st))); dg.add_edges_from(pairs)
    audit[str(year)]={'eligible_records':sum(active(r['tags']) for r in obj['stops']),'unique_locations':len(st),'highway_only':len(strict),'spatial_clusters_50m':nx.number_connected_components(dg),'pbf_sha256':obj['pbf_sha256']}
    if year==2023:
        G,removed=graph(obj)
        audit[str(year)].update({'graph_nodes':G.number_of_nodes(),'graph_edges':G.number_of_edges(),'components':nx.number_connected_components(G),'access_excluded_ways':removed})
        for snap in [100,250]:
            nd,ra=route(G,st,locations,snap); cit.loc[gidx,f'network_{snap}']=nd; audit[str(year)][f'routing_{snap}']=ra
        for snap in [100]:
            nd,ra=route(G,strict,locations,snap); cit.loc[gidx,'network_highway']=nd; audit[str(year)]['routing_highway']=ra
main=cit[cit.verified].copy(); allbar=main[main.reason!='Reports using public transport'].copy(); geo=allbar[allbar.geo].copy()
for metric in ['network_100','network_250']:
    valid=cit[metric].notna()
    assert (cit.loc[valid,metric]>=cit.loc[valid,'d_inclusive_2023']-0.01).all(), 'Network route cannot be shorter than straight-line distance'
assert (cit.loc[cit.geo,'d_inclusive_2023']>=0).all()
order=list(reasonmap.values()); summary=[]
from statsmodels.stats.proportion import proportion_confint
for cohort,d in [('Verified',main),('Full clean',cit)]:
    nb=int((d.reason!='Reports using public transport').sum())
    for reason in order:
        n=int((d.reason==reason).sum()); lo,hi=proportion_confint(n,len(d),method='wilson')
        summary.append({'cohort':cohort,'reason':reason,'n':n,'denominator_all':len(d),'pct_all':100*n/len(d),'pct_reason_givers':100*n/nb if reason!=order[-1] else np.nan,'ci_low_pct':100*lo,'ci_high_pct':100*hi})
pd.DataFrame(summary).to_csv(OUT/'reasons.csv',index=False)
metrics=['d_inclusive_2023','network_100','d_highway_2023','network_250','network_highway','d_inclusive_2026']
rows=[]; tests=[]
for metric in metrics:
    groups=[]
    for reason in order[:-1]:
        a=geo.loc[geo.reason==reason,metric].dropna(); groups.append(a)
        rows.append({'metric':metric,'reason':reason,'n':len(a),'median':a.median(),'q25':a.quantile(.25),'q75':a.quantile(.75)})
    H,p=stats.kruskal(*groups); n=sum(map(len,groups)); eps=max(0,(H-4)/(n-5))
    tests.append({'metric':metric,'n':n,'H':H,'p':p,'epsilon_squared':eps})
pd.DataFrame(rows).to_csv(OUT/'distances_by_reason.csv',index=False)
tt=pd.DataFrame(tests); tt['p_holm']=multipletests(tt.p,method='holm')[1]; tt.to_csv(OUT/'omnibus_tests.csv',index=False)
rng=np.random.default_rng(20260920)
boot=[]
for metric in metrics:
    dd=geo.dropna(subset=[metric]).copy(); blockgroups=[v[[metric,'walk']].to_numpy() for _,v in dd.groupby('block')]; vals=[]
    for _ in range(1999):
        draw=np.concatenate([blockgroups[i] for i in rng.integers(0,len(blockgroups),len(blockgroups))])
        a=draw[draw[:,1]==1,0]; b=draw[draw[:,1]==0,0]
        if len(a) and len(b): vals.append(np.median(a)-np.median(b))
    a=dd.loc[dd.walk==1,metric]; b=dd.loc[dd.walk==0,metric]
    boot.append({'metric':metric,'n_walk':len(a),'n_other':len(b),'blocks':len(blockgroups),'walk_median':a.median(),'other_median':b.median(),'difference':a.median()-b.median(),'ci_low':np.quantile(vals,.025),'ci_high':np.quantile(vals,.975),'valid_bootstraps':len(vals)})
pd.DataFrame(boot).to_csv(OUT/'walking_contrasts.csv',index=False)
# Exploratory adjusted association, no causal or prediction claim.
models=[]
for response in ['walk','habit']:
    dd=geo.dropna(subset=['age','income','d_inclusive_2023','block']).copy(); dd['log_distance']=np.log2(1+dd.d_inclusive_2023/100)
    fit=smf.glm(f'{response} ~ log_distance + age + female + C(income)',dd,family=sm.families.Binomial()).fit(cov_type='cluster',cov_kwds={'groups':dd.block})
    for name,val in fit.params.items():
        ci=fit.conf_int().loc[name]; models.append({'outcome':response,'term':name,'n':len(dd),'blocks':dd.block.nunique(),'OR':np.exp(val),'low':np.exp(ci.iloc[0]),'high':np.exp(ci.iloc[1]),'p':fit.pvalues[name]})
pd.DataFrame(models).to_csv(OUT/'adjusted_associations.csv',index=False)
# Sensitivity to geographic restriction and all 460 cleaned rows.
sens=[]
for label,d in [('Verified 450',main),('Full clean 460',cit),('Verified Truong Tho',main[main.ward=='Trường Thọ'])]:
    d=d[d.geo&(d.reason!=order[-1])]; groups=[d.loc[d.reason==r,'d_inclusive_2023'].dropna() for r in order[:-1]]
    H,p=stats.kruskal(*groups); sens.append({'cohort':label,'n':len(d),'walk_n':int(d.walk.sum()),'habit_n':int(d.habit.sum()),'H':H,'p':p,'median_distance':d.d_inclusive_2023.median()})
pd.DataFrame(sens).to_csv(OUT/'cohort_sensitivity.csv',index=False)
mode=main['Q1.10_PTDiChuyen'].astype(str)
modeout={'motorcycle_reports':int(mode.str.contains('Xe máy cá nhân',regex=False).sum()),'bus_reports':int(mode.str.contains('Xe buýt',case=False,regex=False).sum()),'q28_users':int((main.reason==order[-1]).sum()),'both_bus_and_q28_user':int((mode.str.contains('Xe buýt',case=False,regex=False)&(main.reason==order[-1])).sum())}
result={'clean_n':len(cit),'verified_n':len(main),'unmatched_clean_n':int((~cit.verified).sum()),'verified_geo_n':int(main.geo.sum()),'verified_reason_n':len(allbar),'verified_geo_reason_n':len(geo),'raw_item_checks':checks,'modes':modeout,'osm':audit,'timestamp_min':str(main.Timestamp.min()),'timestamp_max':str(main.Timestamp.max()),'wards':main.ward.value_counts().to_dict(),'versions':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__},'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [args.clean_survey,args.raw_survey]}}
dump('results.json',result)
# Figures contain aggregate distributions only; never household coordinates.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
rr=pd.DataFrame(summary); rr=rr[(rr.cohort=='Verified')&(rr.reason!=order[-1])]
fig,ax=plt.subplots(figsize=(8,3.5)); ax.barh(rr.reason[::-1],rr.pct_reason_givers[::-1],color='#315e79'); ax.set_xlabel('Share of respondents giving a reason (%)'); ax.set_xlim(0,80)
for i,(_,r) in enumerate(rr.iloc[::-1].iterrows()): ax.text(r.pct_reason_givers+1,i,f'{r.pct_reason_givers:.1f}% (n={r.n})',va='center',fontsize=9)
fig.tight_layout(); fig.savefig(OUT/'Figure1_reasons.png',dpi=220); plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(10,4))
for ax,m,title in zip(axes,['d_inclusive_2023','network_100'],['Mapped bus location proximity','Network distance with 100 m connectors']):
    for r in ['Motorcycle habit','Walking discomfort','Stops and frequency','Parking at stops','Bus quality and staff']:
        a=np.sort(geo.loc[geo.reason==r,m].dropna()); ax.step(a,np.arange(1,len(a)+1)/len(a),where='post',label=r)
    ax.set_xlabel('Distance (m)'); ax.set_ylabel('Cumulative share'); ax.set_title(title,fontsize=10); ax.set_xlim(0,2000); ax.set_ylim(0,1)
axes[0].legend(fontsize=7,loc='lower right'); fig.tight_layout(); fig.savefig(OUT/'Figure2_accessibility.png',dpi=220); plt.close(fig)
print(json.dumps(result,ensure_ascii=True,indent=2),flush=True)

if args.make_maps:
    from spatial_figures import build_maps
    build_maps(cit,G,stops(extract(2023)),TR,OUT,args.context_dir)
