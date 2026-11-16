# 🏏 SupeRR Selector 2027 — RR War Room

### Cricket Analytics | Pressure Performance | Data-Driven Player Scouting

**An interactive cricket scouting intelligence dashboard designed to identify T20 batters and bowlers who perform effectively in high-pressure match situations.**

Built using **Python, Pandas, Plotly, Streamlit, and Excel**, the project combines ball-by-ball cricket analysis, context-adjusted performance metrics, ranking stability assessments, and interactive player scouting profiles.

**[🚀 Explore the Live Dashboard](https://superr-selector-2027.streamlit.app/)**

---

## 📌 Project Overview

Traditional cricket statistics, such as total runs, batting average, wickets, and economy rate, do not always capture how effectively players perform when matches become demanding.

**SupeRR Selector 2027** addresses this limitation by evaluating performance in pressure situations using contextual expectations rather than relying exclusively on raw totals.

The project presents its findings through a Rajasthan Royals-inspired scouting dashboard.

**Project objectives:**
- Identify batters who consistently exceed contextual run expectations.
- Evaluate IPL bowlers using pressure-phase run prevention.
- Account for sample size, consistency, and ranking stability.
- Present evidence-backed player recommendations.
- Communicate analytical assumptions and limitations transparently.

> This is an independent educational scouting project and is not affiliated with Rajasthan Royals or the IPL.

## 📊 Dataset Overview

| Metric | Value |
|---|---:|
| Total matches analyzed | 883 |
| Ball-by-ball deliveries | 200,999 |
| IPL matches | 371 |
| T20 International matches | 482 |
| Other T20 matches | 30 |
| Identified pressure opportunities | 46,990 |
| Matches containing pressure opportunities | 831 |
| Shortlisted batters | 10 |
| Shortlisted bowlers | 10 |

**Data coverage:** 2022–2026.

The analysis combines multiple T20 formats while applying IPL-specific evidence requirements to the bowling shortlist.

## 🧠 Analytical Methodology

### 1. Pressure Situation Identification

Pressure opportunities are identified using match-context indicators, including:

- Death-over situations.
- Demanding run chases.
- Competitive, closely contested finishes.

**Important:** Approximately 94.6% of identified pressure opportunities occur during death overs. Consequently, the results primarily describe death-over performance rather than every possible form of cricketing pressure.

Pressure is treated as an observable match-context proxy, not a psychological measurement.

### 2. Context-Adjusted Performance

A contextual expected-runs framework considers factors such as:

- Innings and match phase.
- Chase requirements.
- Wickets remaining.
- Relevant match circumstances.

Contextual estimates are smoothed to reduce instability.

**Batting metric:** Runs Above Expected per 100 Pressure Balls.

This measures how many additional runs a batter scores relative to contextual expectations, standardized to 100 pressure deliveries.

**Bowling metric:** IPL Runs Prevented per 6 Legal Pressure Balls.

This measures a bowler's run prevention relative to contextual expectations, standardized to six legal pressure deliveries.

### 3. Player Qualification

Minimum evidence requirements help prevent extremely small samples from dominating the rankings.

**Batters:**
- At least 200 pressure balls.
- At least 20 pressure matches.
- At least 15 meaningful matches.

**Bowlers:**
- At least 100 IPL legal pressure balls.
- At least 10 IPL pressure matches.

### 4. Player Ranking

Batting rankings incorporate context-adjusted output, dismissal avoidance, consistency, and evidence reliability.

The IPL-aware bowling score uses the following weighting:

| Component | Weight |
|---|---:|
| Overall bowling composite | 50% |
| IPL pressure run prevention | 25% |
| IPL wicket contribution | 15% |
| IPL evidence strength | 10% |

### 5. Ranking Stability

Alternative ranking scenarios are used to examine whether shortlisted players remain competitive when scoring assumptions change.

Eight of the ten proposed bowlers appear in the top ten across all four evaluated ranking scenarios.

**Scouting judgment exception:** Josh Hazlewood was included at proposed selection position 10 despite a calculated model rank of 13, based on broader multi-season IPL evidence.

This exception is disclosed rather than presented as an automatic model recommendation.

---

## 🏆 Selected Scouting Findings

### Top-Ranked Batters

| Rank | Player | Composite Score | Runs Above Expected / 100 Pressure Balls |
|---|---|---:|---:|
| 1 | Tim David | 92.21 | +36.96 |
| 2 | Suryakumar Yadav | 87.46 | +47.49 |
| 3 | Tristan Stubbs | 87.13 | +29.69 |
| 4 | Shashank Singh | 86.80 | +28.99 |
| 5 | Shreyas Iyer | 86.76 | +35.26 |

### Leading IPL-Aware Bowlers

| Proposed Rank | Player | IPL-Aware Score | IPL Runs Prevented / 6 Legal Pressure Balls |
|---|---|---:|---:|
| 1 | Rashid Khan | 87.23 | +0.56 |
| 2 | Sunil Narine | 84.01 | +3.97 |
| 3 | Jasprit Bumrah | 83.16 | +3.00 |
| 4 | Wanindu Hasaranga | 82.56 | +0.97 |
| 5 | Matheesha Pathirana | 79.87 | +1.07 |

These rankings reflect the project's defined methodology and historical dataset, not guaranteed future outcomes.

## 💻 Interactive Dashboard

The Streamlit application includes:

- **Pressure Index:** Dataset coverage and pressure-performance overview.
- **Scouting Spotlight:** Highlighted batting and bowling recommendations.
- **Scouting Philosophy:** Explanation of context-adjusted analysis.
- **Batting Intelligence:** Comparative batting performance.
- **IPL Bowling Intelligence:** Pressure-phase bowling effectiveness.
- **Batting Reliability:** Evidence strength and sample-size considerations.
- **Batting Consistency:** Positive-match performance.
- **Scouting Confidence:** Ranking stability across scenarios.
- **Scouting Centre:** Twenty personalized player profiles with roles, squad-fit assessments, and cautions.
- **Behind the Numbers:** Methodology, qualification rules, assumptions, and limitations.

The dashboard includes **five interactive Plotly charts**.

**[🌐 Launch the RR War Room](https://superr-selector-2027.streamlit.app/)**

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and application development |
| Pandas | Data manipulation and analytical workflows |
| Excel | Analysis outputs and supporting evidence |
| Plotly | Interactive data visualization |
| Streamlit | Interactive dashboard and web application |
| GitHub | Source-code hosting and version control |
| Streamlit Community Cloud | Public application deployment |

## 📁 Repository Structure

```text
SupeRR-Selector-2027/
├── .streamlit/
│   └── config.toml
├── assets/
│   └── players/
│       └── rishabh_pant.png
├── data/
│   ├── ipl_photo_quality_comparison.csv
│   ├── player_image_manifest.csv
│   ├── player_photo_candidates.csv
│   ├── player_scouting_profiles.json
│   └── rishabh_pant_photo_credit.json
├── app.py
├── SupeRR_Selector_Analysis.xlsx
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/Anupam-codes7/SupeRR-Selector-2027.git
cd SupeRR-Selector-2027
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Launch the dashboard**

```bash
streamlit run app.py
```

Open the local address displayed by Streamlit.

## 📈 Project Deliverables

- Interactive cricket scouting dashboard.
- Excel workbook containing player rankings and supporting analyses.
- Context-adjusted batting and bowling comparisons.
- Player consistency and ranking stability assessments.
- Twenty personalized scouting profiles.
- Documented methodology and analytical limitations.
- Publicly deployed Streamlit application.

## ⚠️ Limitations

This project has several important limitations:

1. The analysis is descriptive and historical, not a validated predictive model.
2. Pressure identification is heavily concentrated in death-over situations.
3. Player rankings depend on the selected contextual definitions, qualification thresholds, and scoring weights.
4. Historical performance does not guarantee future performance.
5. Player availability, contracts, squad eligibility, auction rules, and acquisition costs were not evaluated.
6. The proposed scouting shortlist should not be interpreted as a verified, immediately obtainable IPL squad.

## 👨‍💻 Author

**Anupam Das**

B.Tech — Computer Science and Engineering (Data Science)

Interested in Artificial Intelligence, Machine Learning, Data Science, and software engineering.

**GitHub:** [Anupam-codes7](https://github.com/Anupam-codes7)

## 📜 Disclaimer

SupeRR Selector 2027 is an independent educational cricket analytics project.

Rajasthan Royals-inspired visual branding is used for project presentation. The project is not officially associated with Rajasthan Royals, the Indian Premier League, or their respective organizations.
