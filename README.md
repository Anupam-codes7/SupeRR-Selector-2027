# SupeRR Selector 2027 — RR War Room

An independent cricket scouting dashboard developed
using historical IPL, T20I and other T20 ball-by-ball data.

## Features

- Five interactive Plotly charts
- Top 10 pressure-performance batters
- Top 10 IPL-aware bowlers
- Twenty personalized player scouting profiles
- Context-adjusted performance analysis
- Ranking stability analysis
- Model methodology and limitations

## Run Locally

Install dependencies:

    pip install -r requirements.txt

Start the application:

    streamlit run app.py

## Data

The application reads:

    SupeRR_Selector_Analysis.xlsx

Scouting profiles are stored in:

    data/player_scouting_profiles.json

## Important Limitations

The analysis is descriptive rather than predictive.

Player availability, contracts, auction eligibility,
acquisition costs and future performance are not established.

Most identified pressure opportunities occur in death overs.

## Disclaimer

Independent educational scouting analysis.
Not affiliated with Rajasthan Royals or the IPL.
