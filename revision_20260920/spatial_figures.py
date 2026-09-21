"""Publication maps; no exact respondent locations are written or plotted."""
from pathlib import Path
import json, hashlib
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Circle
from scipy.spatial import cKDTree

def build_maps(cit, G, st, transform, out, context):
    out=Path(out); context=Path(context)
    def project(coords):
        a=np.asarray(coords); return np.column_stack(transform.transform(a[:,0],a[:,1]))
    wards=json.loads((context/'wards.geojson').read_text(encoding='utf-8'))
    metro=json.loads((context/'metro.geojson').read_text(encoding='utf-8'))
    tt=next(f for f in wards['features'] if f['properties'].get('Name')=='Truong Tho Ward')
    def rings(f):
        g=f['geometry']; return [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
    boundary=[project(r) for r in rings(tt)]
    rails=[]
    for f in metro['features']:
        if f['properties'].get('ref')!='L1': continue
        g=f['geometry']; parts=g['coordinates'] if g['type']=='MultiLineString' else [g['coordinates']]
        rails.extend(project(x) for x in parts)
    segments=[[(G.nodes[u]['x'],G.nodes[u]['y']),(G.nodes[v]['x'],G.nodes[v]['y'])] for u,v in G.edges]
    d=cit[cit.verified & cit.geo]; xy=project(d[['Long','Lat']].values)
    cells=pd.DataFrame(np.floor(xy/500).astype(int),columns=['gx','gy']).value_counts().rename('n').reset_index()
    shown=cells[cells.n>=5]; hidden=int(cells.loc[cells.n<5,'n'].sum())
    def base(ax):
        ax.set_facecolor('#f6f7f5'); ax.add_collection(LineCollection(segments,colors='#b6bdbb',linewidths=.25,rasterized=True))
        for r in boundary: ax.plot(r[:,0],r[:,1],color='#202e37',lw=1.7)
        for r in rails: ax.plot(r[:,0],r[:,1],color='#9564a4',lw=1.6,ls='--')
        ax.scatter(st.x,st.y,s=9,c='#087f8c',alpha=.75,edgecolors='none')
        ax.scatter((shown.gx+.5)*500,(shown.gy+.5)*500,s=20+shown.n*3,c='#dc8432',alpha=.8,edgecolors='white',linewidths=.4)
        ax.set_aspect('equal'); ax.tick_params(labelsize=7)
        ax.ticklabel_format(style='plain',useOffset=False)
        ax.xaxis.set_major_locator(MaxNLocator(4)); ax.yaxis.set_major_locator(MaxNLocator(5))
        ax.set_xlabel('UTM easting (m)',fontsize=8);ax.set_ylabel('UTM northing (m)',fontsize=8)
    fig,axs=plt.subplots(1,2,figsize=(11,5.8))
    for ax in axs:base(ax)
    corners=project([[106.66,10.74],[106.85,10.92]])
    axs[0].set_xlim(corners[:,0]);axs[0].set_ylim(corners[:,1]);axs[0].set_title('(a) Extraction window in eastern Ho Chi Minh City',fontsize=10)
    bb=np.vstack(boundary);lo=bb.min(axis=0)-1000;hi=bb.max(axis=0)+1000
    axs[1].set_xlim(lo[0],hi[0]);axs[1].set_ylim(lo[1],hi[1]);axs[1].set_title('(b) Truong Tho and surrounding mapped streets',fontsize=10)
    for ax,length in zip(axs,[3000,1000]):
        x0,x1=ax.get_xlim();y0,y1=ax.get_ylim();x=x0+.06*(x1-x0);y=y0+.07*(y1-y0)
        ax.plot([x,x+length],[y,y],color='black',lw=2);ax.text(x,y+.015*(y1-y0),f'{length/1000:g} km',fontsize=8)
        ax.annotate('N',xy=(.94,.96),xytext=(.94,.85),xycoords='axes fraction',ha='center',arrowprops={'arrowstyle':'->'},fontsize=9)
    handles=[Line2D([],[],color='#202e37',label='Archived Truong Tho outline'),Line2D([],[],color='#9564a4',ls='--',label='Metro Line 1 context'),Line2D([],[],marker='o',ls='',color='#087f8c',label='OSM bus locations, 2023'),Line2D([],[],marker='o',ls='',color='#dc8432',label='Survey cell centres (500 m; n >= 5)')]
    fig.legend(handles=handles,loc='lower center',ncol=2,fontsize=8,frameon=False)
    fig.subplots_adjust(bottom=.18,wspace=.29,top=.92)
    fig.savefig(out/'Figure1_study_area.png',dpi=300);fig.savefig(out/'Figure1_study_area.pdf');plt.close(fig)

    # Select a deterministic synthetic origin from public graph geometry only.
    ids=list(G);pos=np.array([[G.nodes[i]['x'],G.nodes[i]['y']] for i in ids]);tree=cKDTree(pos)
    stopxy=st[['x','y']].values;ds,si=tree.query(stopxy)
    H=G.copy();H.add_node(-1)
    for dd,j in zip(ds,si):
        if dd<=100 and (not H.has_edge(-1,ids[j]) or H[-1][ids[j]]['weight']>dd):H.add_edge(-1,ids[j],weight=float(dd))
    distance,paths=nx.single_source_dijkstra(H,-1)
    centre=bb.mean(axis=0); candidates=np.argsort(np.linalg.norm(pos-centre,axis=1))
    selected=None
    for j in candidates[::17]:
        origin=pos[j]+[35,25];connector,k=tree.query(origin);node=ids[k]
        straight,nearest=cKDTree(stopxy).query(origin)
        total=distance.get(node,np.inf)+connector
        if 150<straight<650 and np.isfinite(total) and 1.3<total/straight<3 and total<1200:
            selected=(origin,connector,node,straight,nearest,total);break
    if selected is None:raise RuntimeError('No suitable public-geometry illustration origin')
    origin,connector,node,straight,nearest,total=selected;path=paths[node][1:][::-1]
    target=path[-1];options=[i for i,j in enumerate(si) if ids[j]==target and ds[i]<=100]
    end=min(options,key=lambda i:ds[i]);route=np.vstack([origin,[[G.nodes[i]['x'],G.nodes[i]['y']] for i in path],stopxy[end]])
    fig,ax=plt.subplots(figsize=(9,6));ax.set_facecolor('#f6f7f5')
    ax.add_collection(LineCollection(segments,colors='#b4bdbb',linewidths=.7,rasterized=True))
    ax.scatter(st.x,st.y,s=32,c='#087f8c',label='Mapped bus location')
    ax.plot(route[:,0],route[:,1],color='#bf4c3a',lw=2.8,label=f'Network + connectors: {total:.0f} m')
    ax.plot([origin[0],stopxy[nearest,0]],[origin[1],stopxy[nearest,1]],ls='--',color='#3266aa',lw=2,label=f'Nearest-stop straight line: {straight:.0f} m')
    for pair in [route[:2],route[-2:]]:ax.plot(pair[:,0],pair[:,1],color='#d39920',lw=3,ls=':',zorder=6)
    ax.add_patch(Circle(origin,100,fill=False,color='#555555',ls='--',lw=1,label='100 m origin connector limit'))
    ax.scatter(*origin,marker='*',s=180,color='#202e37',zorder=8,label='Synthetic origin (not a respondent)')
    ax.annotate('Synthetic origin',origin,xytext=(12,14),textcoords='offset points',fontsize=9)
    extent=np.vstack([route,stopxy[nearest]]);lo=extent.min(axis=0)-170;hi=extent.max(axis=0)+170
    ax.set_xlim(lo[0],hi[0]);ax.set_ylim(lo[1],hi[1]);ax.set_aspect('equal');ax.ticklabel_format(style='plain',useOffset=False);ax.tick_params(labelsize=8)
    ax.set_xlabel('UTM easting (m)');ax.set_ylabel('UTM northing (m)')
    ax.set_title('Mapped routing geometry, not an observed walking route',fontsize=12)
    ax.legend(loc='upper left',bbox_to_anchor=(1.01,1),fontsize=8,frameon=False)
    fig.subplots_adjust(right=.66,bottom=.13)
    fig.savefig(out/'Figure2_network_method.png',dpi=300,bbox_inches='tight');fig.savefig(out/'Figure2_network_method.pdf',bbox_inches='tight');plt.close(fig)
    audit={'survey_geolocated_n':len(d),'grid_m':500,'minimum_cell_n':5,'displayed_respondents':int(shown.n.sum()),'suppressed_respondents':hidden,'displayed_cells':len(shown),'exact_respondent_points_published':False,'illustration_origin':'synthetic, selected solely from public OSM graph','illustration_straight_m':float(straight),'illustration_network_m':float(total),'illustration_origin_connector_m':float(connector),'illustration_stop_connector_m':float(ds[end]),'illustration_same_stop':bool(end==nearest),'context_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in context.glob('*.geojson')}}
    assert connector<=100 and ds[end]<=100 and total>=straight
    (out/'map_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
