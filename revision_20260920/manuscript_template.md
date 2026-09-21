# Beyond distance to a bus stop

Stated barriers and historically mapped transit access in Ho Chi Minh City

## Abstract

Proximity to a public transport stop measures only part of the conditions under which people decide to travel. This study examines stated barriers and mapped bus access before Metro Line 1 opened in Ho Chi Minh City. We link {{N}} source-verified respondents from a 2023 urban living lab survey to historical OpenStreetMap data. The analysis preserves five barrier categories and distinguishes bus-location proximity from network distance and walking comfort. Among {{NB}} respondents giving a reason for non-use, {{HABIT_N}} selected motorcycle habit and {{WALK_N}} selected walking discomfort. {{ABSTRACT_RESULTS}} These estimates do not establish equivalence between groups or identify the cause of non-use. A later map snapshot tests sensitivity to mapping coverage, rather than measuring infrastructure delivery or behavioural change. The contribution is a reproducible procedure for aligning survey constructs, map definitions and policy claims. Short mapped distances cannot dismiss reported discomfort, while a single habit response cannot establish that infrastructure investment is ineffective. First-mile planning should combine historical network evidence with direct assessment of walking conditions and service quality.

Keywords: public transport; stated barriers; walking access; historical OpenStreetMap; motorcycle use; Vietnam

## 1 Introduction

Improving public transport requires understanding both the transport opportunities available to people and the conditions under which they can use them. Accessibility research has long distinguished access to opportunities from movement itself, and has shown that the choice of an indicator shapes the diagnosis of a transport problem ({{Geurs2004}}; {{Handy1997}}). Nevertheless, a short distance to a stop is easily interpreted as evidence that an access problem has been solved. This interpretation becomes especially consequential when a resident reports an impediment that a map does not measure.

Ho Chi Minh City offers a relevant setting for examining this problem. Research on mobility in Vietnamese cities situates motorcycle travel within social practices and aspirations, rather than treating vehicle use as a response to travel time alone ({{Truitt2008}}; {{Hansen2017}}). Local studies have examined psychological determinants of bus-use intention, preferences involving new transport modes, and the potential shift from motorcycles to public transport ({{Bus2009}}; {{Modal2019}}; {{Bayes2024}}). These perspectives make it important to distinguish what people report, what spatial indicators represent and what either source can establish about policy.

The Truong Tho Living Lab collected resident responses in 2023, before Metro Line 1 commenced commercial operation on 22 December 2024 ({{JICA2024}}). The questionnaire asked which transport modes respondents used and required one answer to a question about reasons for not using public transport. The choices included motorcycle habit, discomfort walking to stops, insufficient stops and frequency, inadequate parking, and bus quality and staff conduct. These categories refer to different dimensions of a journey. Their relationship to a common distance indicator is therefore an empirical question, not a contest in which either survey or map must be correct.

This article makes a bounded contribution to transport policy diagnosis. It links those responses to historical bus-location and street-network data while auditing the survey denominator, the transport features admitted to the map and the assumptions needed to compute a walking route. The historical perspective matters because a facility can be mapped before it opens, and a later mapping edit can alter a distance without any corresponding change in service. The contribution is not a causal estimate of metro impacts, a citywide modal-share estimate or a test that infrastructure does not matter.

Three questions organise the analysis. First, which reasons were recorded among respondents with traceable source records, and how should their percentages be interpreted? Second, how do historically mapped distances vary across those reasons, particularly between respondents reporting walking discomfort and those giving other reasons? Third, how sensitive are the comparisons to the definition of a bus location, network connection rules and the cohort included? These questions support a practical distinction between an access indicator and the wider service problem it is sometimes asked to represent.

## 2 Conceptual framework

### 2.1 Calculated access and reported experience

Calculated and perceived accessibility are related but non-identical constructs. Pot and colleagues explain why mismatches may arise from awareness and from the inability of an indicator to represent subjective evaluations ({{Pot2021}}). Work developing and applying the Perceived Accessibility Scale makes the individual experience of access an explicit object of measurement ({{Lattman2016}}; {{Lattman2018}}). The present questionnaire does not contain that scale. A selected reason for non-use should therefore not be relabelled as a validated measure of perceived accessibility.

The distinction also concerns the policy objective. Accessibility research identifies challenges in connecting indicators to the questions that planning should answer ({{VanWee2016}}), while research on accessibility planning asks whether operational practice addresses what matters to users ({{Curl2015}}). A distributive perspective further requires attention to who can benefit from a transport system rather than relying only on average provision ({{Geurs2016}}). In this study, distance is interpreted as one component of first-mile access. It does not incorporate destinations, timetable connectivity, monetary costs or a person's ability to complete the trip.

### 2.2 Habit as a response rather than an established mechanism

Theories of planned behaviour and research on repeated action provide reasons to study intentions, attitudes and habitual processes together ({{Ajzen1991}}; {{Aarts1998}}; {{Bamberg2003}}). However, the word habit in a response option is not interchangeable with a measured psychological construct. The Self-Report Habit Index and subsequent work on automaticity explicitly use measurement instruments that are absent here ({{Verplanken2003}}; {{Gardner2012}}). We consequently refer to a habit response or stated motorcycle habit, not an independently established level of automaticity.

Travel research has examined habit and motivation in stable contexts, experimental disruption through a free bus ticket, and the role of behavioural measures in transport policy ({{Gardner2009}}; {{Fujii2003}}; {{Bamberg2011}}). Other work cautions against oversimplifying habits and the direction of relationships between attitudes and behaviour ({{Schwanen2012}}; {{Kroesen2017}}). Instrumental, symbolic and affective motives can also coexist ({{Steg2005}}). These contributions support treating a single selected response as a limited description. They do not justify interpreting its prevalence as the share of a population whose behaviour is immune to infrastructure improvement.

### 2.3 Distance is not walking comfort

Built-environment research relates travel to density, diversity and design, while broader synthesis documents variation across transport and land-use measures ({{Cervero1997}}; {{Ewing2010}}). For walking, the relevant attributes extend beyond proximity: environmental correlates, urban design qualities and the hierarchy of walking needs all identify reasons why similar distances can be experienced differently ({{Saelens2003}}; {{Ewing2009}}; {{Alfonzo2005}}). Operational reviews of active accessibility and work on non-motorised access likewise show that measurement choices require explicit justification ({{Vale2015}}; {{Iacono2010}}).

Empirical research on distances to transit stops cautions against treating one fixed catchment as universally representative ({{ElGeneidy2014}}). In Ho Chi Minh City, the multiple uses of sidewalks also make the street edge more than a neutral movement corridor ({{Kim2012}}). A mapped route does not verify an unobstructed sidewalk, safe crossing, shade or a suitable surface. A lack of a detected distance difference therefore cannot reclassify walking discomfort as merely perceptual. Conversely, a difference in distance would not by itself establish that distance caused the response.

### 2.4 Historical maps as partial evidence

OpenStreetMap is a form of volunteered geographic information whose utility depends on how contributors record the world ({{Goodchild2007}}; {{Neis2012}}). Research on its accuracy and road completeness provides a basis for using it critically, not a guarantee that every local transport feature is complete or operational ({{Haklay2010}}; {{Barrington2017}}). Reproducible street-network analysis makes such definitions inspectable ({{Boeing2017}}). Our analysis uses a custom extraction with explicit feature and access rules; it does not imply that a software package can substitute for a local service inventory.

This framework generates a modest expectation: different reasons may overlap in mapped distance because they concern partially different dimensions of access. The analysis estimates that overlap and its uncertainty. It does not assume in advance that overlap will occur, that the groups are equivalent, or that an observed mismatch identifies which policy instrument should receive the largest budget.

## 3 Study setting and data

Figure 1 locates the historical bus map and survey coverage in eastern Ho Chi Minh City, southern Vietnam. Survey locations are displayed only as centres of 500 m cells containing at least five source-linked respondents; smaller cells are suppressed. Symbol sizes represent cell counts, not individual addresses. The archived Truong Tho outline and Metro Line 1 alignment provide geographic context only. Their dates are not independently certified as 2023 boundaries or infrastructure states, and neither layer enters distance calculations.

[[FIGURE1]]

### 3.1 Survey provenance and analytical population

The resident questionnaire belongs to a wider urban living lab programme centred on Truong Tho in the then Thu Duc City. Respondents also lived in adjoining and other wards. The analysis treats the sample as an observational local case, with no probability-sampling weights or claim of representativeness for Ho Chi Minh City. The available source export contains {{N}} resident records. The cleaned workbook contains 460, of which {{N}} can be linked to that export by timestamp. The ten additional cleaned records are retained only in a sensitivity analysis pending reconciliation of their provenance.

The main analysis uses the source-linked cohort and checks the original response fields against the cleaned file. Where transport-response text differs, the source export takes precedence for the verified cohort. {{PROVENANCE_TEXT}} Timestamps document data entry between {{DATE_MIN}} and {{DATE_MAX}}; they are not independent evidence of each interview's field date. The study is described as a 2023 survey, not as a panel or an immediately pre-opening evaluation.

The analytical denominator changes with the question. Mode reporting uses all {{N}} source-linked records. Barrier comparisons exclude {{NU}} respondents whose recorded answer says they use public transport, leaving {{NB}} reason-givers. Geographic analysis further requires coordinates within the extraction region. {{NG}} verified records meet that rule, of which {{NBG}} give a reason. Network comparisons may contain fewer observations because not every location can be connected under the specified rule. Table 1 states these denominators explicitly.

[[TABLE1]]

### 3.2 Questionnaire interpretation

The mode item asks which modes the respondent uses in the city and explicitly permits more than one answer. A report of motorcycle use is therefore not a trip share or necessarily a principal mode. The barrier item requests one answer. It cannot measure all simultaneous barriers or rank the importance of unselected alternatives. Moreover, the stop option combines stop numbers and service frequency, although the map measures only the spatial component.

The archived questionnaire lists five reasons. The response export additionally contains the answer that the person uses public transport. We preserve that answer and report it separately rather than forcing it into a barrier category. The apparent inconsistency across items is informative about measurement limits: listing bus use and declining to give a non-use reason are not interchangeable definitions of a public transport user. Neither should be used to infer a validated frequency of travel.

Demographic covariates are age in 2023, recorded gender and household income band. For exploratory adjusted associations, the sparse upper income categories are combined into an above-VND-15-million group, compared with below VND 5 million and VND 5–15 million. Income is treated categorically. No coefficient is interpreted as an affordability mechanism, and no household is assumed to have the same disposable resources simply because it belongs to the same band.

### 3.3 Public data and temporal alignment

The core public source is the historical Vietnam OpenStreetMap extract labelled 1 January 2023, with a second extract labelled 1 January 2026 used as a mapping-sensitivity comparison ({{Geofabrik2026}}). File hashes and extraction rules accompany the analysis. Coordinates are projected to UTM zone 48N, and the extraction window is 106.66–106.85°E and 10.74–10.92°N. This window is a computational boundary, not a definition of the sampled population or the administrative extent of Truong Tho.

Bus candidates are features explicitly tagged as bus stops, bus stations or bus-related transport objects. Rail station, halt, stop, proposed and construction features are excluded from this bus set, as are records explicitly marked inactive or inaccessible under the implemented rules. Identical coordinate pairs are collapsed. A narrower sensitivity definition admits only highway=bus_stop. The resulting objects are mapped bus locations, not a verified register of operational stops. The available files do not provide a validated historical timetable, service-frequency series or complete record of opening dates.

The 2026 extract cannot explain a response made in 2023. Its role is to show how much a diagnostic result can depend on the map version and tagging definition. The study does not estimate before–after ridership, mode switching or the effect of Metro Line 1. Population projections, satellite built-up indices and provincial business rankings are omitted from the main design because they do not directly resolve the relationship between a selected travel barrier and first-mile access.

## 4 Methods

Figure 2 illustrates the routing procedure on the extracted 2023 graph. The origin is synthetic, selected solely from public street geometry; it is not a displaced or identifiable survey household. The straight-line nearest stop and network-optimal stop need not be the same. Dotted connectors join endpoints to their nearest admissible graph nodes within 100 m; they are geometric approximations, not verified footpaths. The continuous route is the shortest mapped path under the implemented rules, not an observed or field-validated walking route.

[[FIGURE2]]

### 4.1 Proximity and network construction

Straight-line distance is the minimum projected distance from each valid respondent coordinate to an eligible mapped bus location. We distinguish this measure from a walking route and from access to destinations through public transport. Exact-coordinate duplicates do not affect the minimum distance. Counts of candidate features and clusters within 50 m are provided to show that mapped objects should not automatically be counted as distinct service stops. Cluster counts do not enter the distance calculation.

The walking graph retains original OpenStreetMap node identifiers. Consecutive nodes on an admitted way become undirected edges weighted by projected length; coincident coordinates with different identifiers are not automatically joined. This avoids manufacturing connections at grade-separated crossings. The admitted highway classes cover pedestrian paths and ordinary streets, while cycleways require an explicit permissive foot tag. Ways tagged foot=no or foot=private are removed. General access restrictions are also respected unless an explicit permissive pedestrian tag overrides them.

Both origins and bus locations are connected to the nearest eligible graph node. The primary connector limit is 100 m, with 250 m as a sensitivity analysis. These connectors approximate missing access segments; they do not establish a legal passage through a wall or across private land. A multi-source shortest-path calculation finds the nearest reachable bus location, including connector lengths. Unreachable origins remain missing rather than being replaced with straight-line distances. The graph represents plausible mapped connections, not an audited pedestrian environment.

### 4.2 Descriptive comparisons and uncertainty

We retain the five substantive response categories throughout. Proportions are accompanied by Wilson intervals ({{Wilson1927}}), interpreted as descriptive uncertainty under a simple binomial model rather than design-based population intervals. Distance distributions are reported as medians and interquartile ranges. Exploratory Kruskal–Wallis comparisons are supplied with effect-size estimates and Holm adjustment across the six distance specifications ({{Holm1979}}). Because those tests do not account fully for spatial dependence or the non-probability sample, they do not carry the primary interpretation.

The principal targeted comparison is the median distance among respondents selecting walking discomfort minus the median among respondents giving another substantive reason. To retain some local dependence, we resample occupied 500 m projected grid cells with replacement, keeping all observations within each selected cell. Percentile intervals use 1,999 resamples and a fixed random seed. These intervals describe sampling variability conditional on the observed cohort and grid. They cannot account for missing survey coverage, unknown route quality or uncertainty in the map itself.

Two exploratory binomial models examine walking discomfort and the habit response separately. Each relates the response to log2(1 + distance/100), age, recorded gender and the three income groups. Standard errors are clustered by the same grid cells. The transformed distance coefficient refers to a doubling of the quantity 1 + distance/100, not a constant change per 100 m. Complete-case denominators and cell counts are reported. The models describe conditional association; they do not identify a behavioural mechanism or predict a post-metro outcome.

### 4.3 Sensitivity and interpretation rules

Sensitivity checks vary the bus-feature definition, connector threshold, map year and inclusion of all 460 cleaned records. A further restriction retains only source-verified residents reporting a Truong Tho home address. This last comparison addresses the geographic breadth of recruitment without claiming to make the sample representative. Network missingness is shown alongside results so that a change in the estimated distribution is not silently attributed only to a change in the metric.

We do not interpret a large p-value as proof of no relationship ({{Wasserstein2016}}). Equivalence would require defensible bounds and an appropriate design, not merely failure to reject a conventional null ({{Lakens2017}}). More generally, spatial dependence limits the independence assumptions behind ordinary validation and uncertainty procedures ({{Roberts2017}}). These rules are particularly relevant where a small response category is compared with a much larger habit group. The analysis was developed retrospectively and is not described as preregistered.

## 5 Results

### 5.1 Recorded modes and reasons

{{RESULT_MODES}}

{{RESULT_REASONS}}

[[TABLE2]]

### 5.2 What the historical map contains

{{RESULT_OSM}}

[[TABLE3]]

The distinction between mapped locations and operating services remains important after filtering. Explicit bus tags improve mode specificity, but do not verify that a vehicle called at a location at the survey date. Similarly, removing a prohibited edge does not confirm that the remaining route is comfortable or safe. The public data add reproducible spatial evidence while leaving several dimensions of the questionnaire unmeasured.

### 5.3 Distance distributions and walking discomfort

{{RESULT_DISTANCES}}

[[TABLE4]]

[[FIGURE3]]

[[FIGURE4]]

{{RESULT_CONTRASTS}}

[[TABLE5]]

### 5.4 Adjusted associations and sensitivity

{{RESULT_MODELS}}

{{RESULT_SENSITIVITY}}

These comparisons concern correspondence between recorded responses and constructed indicators. The network and straight-line samples are not identical where routing fails. A change across specifications can therefore reflect both a different exposure definition and selection into the routable subset. The supplementary tables provide denominators for every specification, along with full coefficient estimates and the cohort restrictions.

## 6 Discussion

### 6.1 What the combined evidence contributes

The analysis contributes a disciplined link between a legacy survey and public spatial data. The two sources answer different questions: the survey records one selected account of non-use, while the map describes certain spatial opportunities available under explicit definitions. Combining them makes those differences visible. It does not make the map a complete external criterion against which a resident's account can be declared accurate or mistaken.

This distinction changes the practical reading of a frequent habit response. The response identifies a useful subject for follow-up, but it does not allocate a causal share of non-use to habit. Service limitations, parking arrangements and familiar routines may coexist. An individual can have adopted a motorcycle routine partly because the alternatives have been inconvenient. The cross-sectional data cannot establish the temporal sequence. Studies of built-environment relationships and residential self-selection underline the broader difficulty of separating association, selection and causation ({{Handy2005}}; {{Cao2009}}).

The same reasoning applies to walking discomfort. Two residents with similarly short mapped routes may face different crossings, mobility limitations, exposure to heat or constraints on accompanying children. Those are hypotheses requiring direct observations; they are not findings of this dataset. Their plausibility explains why a distance comparison cannot settle the physical-versus-perceptual status of the reported barrier. The empirical contribution is to show what the available indicator can test and where further diagnosis is necessary.

### 6.2 Implications for first mile policy

The results support a staged diagnostic approach. First, establish which locations were mapped as bus-related at the relevant date and how residents can reach them under transparent network assumptions. Second, investigate the actual content of a reported impediment. A combined stops-and-frequency answer requires both a spatial inventory and service information. A parking answer requires an assessment of parking availability, cost and security. A discomfort answer requires observation of the walking environment and the user's needs. These are different follow-up tasks, even when the same stop serves the respondents.

Third, connect the diagnosis to a testable intervention rather than inferring effectiveness from the prevalence of a reason. Behavioural measures can be combined with improvements in access and service; sustainable mobility is not reducible to one instrument ({{Banister2008}}). Evidence on electric-bus intentions in Vietnam also situates vehicle innovation within a wider set of user concerns ({{Electric2023}}). The present study cannot estimate the effect of an information campaign, additional parking or a new feeder service. It helps specify what would need to be measured to evaluate each of them.

A useful follow-up design would repeat the relevant questions while collecting actual trip frequency, multiple concurrent barriers, perceived-accessibility items and a short route audit. The repeat should distinguish existing bus use from metro uptake and retain the ability to link records only where consent permits. Public timetables or an independently verified service inventory would allow an analysis of waiting time and destination access. These additions would address identifiable measurement gaps, rather than simply enlarging the set of remote-sensing covariates.

### 6.3 Reusing historical data without creating a false before and after study

The value of the 2023 survey is that it records responses before metro operation. That does not make it a quasi-experiment. A second map is not a second behavioural wave, and a station's presence in an early map does not establish that it was available for passenger use. Retaining these distinctions prevents a baseline archive from being stretched into an impact evaluation it cannot support.

The later snapshot remains useful for an auditable reason: it tests how a spatial description changes when coverage and tags change. Policy analysts often work with whatever map is currently downloadable. For a historical survey, this can create a temporal mismatch that is difficult to detect once derived distances have been saved. Keeping source filenames, hashes, extraction rules and dates with the analysis makes the mismatch reviewable. For operational decisions, however, even a reproducible map should be checked against the service that passengers actually encounter.

### 6.4 Limitations and scope of transfer

Several limitations bound the contribution. The local cohort is not a probability sample, and the ten additional cleaned records have not yet been reconciled to the available source export. Timestamp matching improves provenance but does not independently verify interview conduct or recruitment. The sensitivity analysis indicates how inclusion changes the observed results; it cannot resolve the missing documentation. Source records and coordinates remain restricted because they contain identifying information.

The single-choice barrier item is coarse and combines concepts that should be measured separately. The mode question does not record trip counts, and public transport use is inconsistently represented across items. The study therefore cannot estimate modal share, a dose of habit, or the prevalence of every barrier. Small categories also limit precision and the complexity of an appropriate adjusted model.

The OSM feature set has incomplete service metadata. Nearest-node connectors approximate access rather than observe it; the graph excludes explicit prohibitions but cannot recover untagged restrictions. Finite extraction boundaries and disconnected components can affect routes. The 100 m and 250 m checks expose part of this sensitivity without validating all possible paths. No route-level comfort, fares or historical headways are measured.

Finally, the findings are observational. Spatial block resampling and clustered standard errors address only part of the dependence problem and do not remove confounding or selection. Transfer to other cities concerns the measurement and audit procedure, not the numerical response shares. The appropriate general claim is that a planning diagnosis should match each indicator to the construct it can measure and retain unresolved dimensions as explicit evidence needs.

## 7 Conclusion

Linking a 2023 resident survey to historical public maps provides a useful but bounded account of first-mile access in a motorcycle-oriented urban setting. The revised analysis preserves the original barrier categories, uses a source-traceable main cohort and makes bus-feature and walking-network definitions explicit. It also reports uncertainty and sensitivity instead of treating a non-significant comparison as a proof of equivalence.

The policy implication is a requirement for better diagnosis. A short route to a mapped bus location does not establish comfortable access, and a habit response does not establish that infrastructure is irrelevant. Historical survey evidence is most useful when it identifies which combinations of spatial access, service conditions and reported experience need to be examined together. Future evaluation should add verified service information and repeated behavioural observations before attributing change to metro operation or any associated intervention.

## Data and code availability

The revision package contains the analysis script, source-file hashes, aggregate tables, figure-generation code and bibliographic verification records. Source survey records and household coordinates are not included in the shareable outputs. Reproduction of the spatial analysis requires authorised access to the survey files and the named historical extracts. OpenStreetMap-derived data are credited to OpenStreetMap contributors and are subject to the Open Database Licence ({{OSM2026}}). No repository DOI or unrestricted microdata availability is claimed.

## Relationship to other manuscripts

This article is a secondary analysis of the 2023 Truong Tho Living Lab survey programme. Related manuscripts address stakeholder priority differences, spatial clustering of environmental appraisals, and flooding appraisals linked to environmental data. The present analysis focuses on transport-response interpretation and historically mapped bus access; it does not present the shared cohort as a new independent survey. Details of related submissions should accompany the editorial disclosure while preserving the journal's review anonymity requirements.

## References

[[REFERENCES]]
