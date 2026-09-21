# Supplementary tables and reproducibility details

All figures are descriptive or exploratory. Main reference list contains exactly 50 distinct entries.

## omnibus_tests.csv

| metric | n | H | p | epsilon_squared | p_holm |
| --- | --- | --- | --- | --- | --- |
| d_inclusive_2023 | 438 | 9.4727 | 0.0503 | 0.0126 | 0.3019 |
| network_100 | 437 | 6.9665 | 0.1377 | 0.0069 | 0.5507 |
| d_highway_2023 | 438 | 9.4727 | 0.0503 | 0.0126 | 0.3019 |
| network_250 | 437 | 6.9665 | 0.1377 | 0.0069 | 0.5507 |
| network_highway | 437 | 6.9665 | 0.1377 | 0.0069 | 0.5507 |
| d_inclusive_2026 | 438 | 2.0251 | 0.7311 | 0.0000 | 0.7311 |

## walking_contrasts.csv

| metric | n_walk | n_other | blocks | walk_median | other_median | difference | ci_low | ci_high | valid_bootstraps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| d_inclusive_2023 | 68 | 370 | 61 | 281.6455 | 274.2751 | 7.3704 | -71.8230 | 152.8869 | 1999 |
| network_100 | 68 | 369 | 60 | 428.0253 | 424.2722 | 3.7531 | -138.9014 | 191.9557 | 1999 |
| d_highway_2023 | 68 | 370 | 61 | 281.6455 | 274.2751 | 7.3704 | -82.2973 | 152.3450 | 1999 |
| network_250 | 68 | 369 | 60 | 428.0253 | 424.2722 | 3.7531 | -140.3492 | 202.1494 | 1999 |
| network_highway | 68 | 369 | 60 | 428.0253 | 424.2722 | 3.7531 | -141.7897 | 203.6342 | 1999 |
| d_inclusive_2026 | 68 | 370 | 61 | 133.6829 | 141.1018 | -7.4189 | -49.6663 | 33.2468 | 1999 |

## adjusted_associations.csv

| outcome | term | n | blocks | OR | low | high | p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| walk | Intercept | 438 | 61 | 0.1674 | 0.0478 | 0.5859 | 0.0052 |
| walk | C(income)[T.Low] | 438 | 61 | 2.7742 | 1.3242 | 5.8116 | 0.0068 |
| walk | C(income)[T.Middle] | 438 | 61 | 1.4176 | 0.6638 | 3.0278 | 0.3674 |
| walk | log_distance | 438 | 61 | 1.0957 | 0.7578 | 1.5844 | 0.6271 |
| walk | age | 438 | 61 | 0.9893 | 0.9660 | 1.0131 | 0.3752 |
| walk | female | 438 | 61 | 0.8142 | 0.5110 | 1.2972 | 0.3871 |
| habit | Intercept | 438 | 61 | 1.7025 | 0.6390 | 4.5358 | 0.2872 |
| habit | C(income)[T.Low] | 438 | 61 | 0.5450 | 0.2747 | 1.0811 | 0.0824 |
| habit | C(income)[T.Middle] | 438 | 61 | 0.7840 | 0.3718 | 1.6533 | 0.5226 |
| habit | log_distance | 438 | 61 | 0.7698 | 0.5762 | 1.0285 | 0.0767 |
| habit | age | 438 | 61 | 1.0260 | 1.0096 | 1.0426 | 0.0018 |
| habit | female | 438 | 61 | 1.2538 | 0.8264 | 1.9024 | 0.2876 |

## cohort_sensitivity.csv

| cohort | n | walk_n | habit_n | H | p | median_distance |
| --- | --- | --- | --- | --- | --- | --- |
| Verified 450 | 438 | 68 | 309 | 9.4727 | 0.0503 | 276.8249 |
| Full clean 460 | 445 | 71 | 313 | 8.6714 | 0.0699 | 283.5511 |
| Verified Truong Tho | 245 | 35 | 179 | 12.1752 | 0.0161 | 264.6897 |

## reasons.csv

| cohort | reason | n | denominator_all | pct_all | pct_reason_givers | ci_low_pct | ci_high_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Verified | Motorcycle habit | 309 | 450 | 68.6667 | 70.3872 | 64.2383 | 72.7791 |
| Verified | Walking discomfort | 68 | 450 | 15.1111 | 15.4897 | 12.0981 | 18.7147 |
| Verified | Stops and frequency | 29 | 450 | 6.4444 | 6.6059 | 4.5242 | 9.1020 |
| Verified | Parking at stops | 22 | 450 | 4.8889 | 5.0114 | 3.2504 | 7.2910 |
| Verified | Bus quality and staff | 11 | 450 | 2.4444 | 2.5057 | 1.3703 | 4.3236 |
| Verified | Reports using public transport | 11 | 450 | 2.4444 | nan | 1.3703 | 4.3236 |
| Full clean | Motorcycle habit | 313 | 460 | 68.0435 | 70.1794 | 63.6478 | 72.1403 |
| Full clean | Walking discomfort | 71 | 460 | 15.4348 | 15.9193 | 12.4208 | 19.0213 |
| Full clean | Stops and frequency | 29 | 460 | 6.3043 | 6.5022 | 4.4250 | 8.9074 |
| Full clean | Parking at stops | 22 | 460 | 4.7826 | 4.9327 | 3.1793 | 7.1349 |
| Full clean | Bus quality and staff | 11 | 460 | 2.3913 | 2.4664 | 1.3404 | 4.2308 |
| Full clean | Reports using public transport | 14 | 460 | 3.0435 | nan | 1.8214 | 5.0433 |