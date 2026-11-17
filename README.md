# SupeRR Selector 2027 — RR War Room

## Independent Cricket Analytics and Player Scouting Dashboard

An interactive cricket analytics project that evaluates historical
T20 batting and bowling performance under pressure.

The project uses historical IPL, T20I, and other T20 ball-by-ball
data to support transparent, data-informed scouting discussions.

This is an independent educational project and is not affiliated
with Rajasthan Royals or the Indian Premier League.

---

## Project Overview

Traditional cricket statistics do not always capture the match
situations in which runs are scored or wickets are taken.

SupeRR Selector explores historical performance under pressure
through context-adjusted player comparisons.

The analysis is descriptive rather than predictive.

## Dashboard Features

- Top 10 pressure-performance batters
- Top 10 IPL-aware bowlers
- 20 personalized player scouting profiles
- Five interactive Plotly charts
- Context-adjusted player comparisons
- Bowling ranking stability analysis
- Model methodology and limitations

## Technology Stack

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL
- Microsoft Excel
- Git and GitHub

## Project Structure

Main application: app.py

Analytical workbook: SupeRR_Selector_Analysis.xlsx

Dependencies: requirements.txt

Streamlit configuration: .streamlit/config.toml

Scouting profiles: data/player_scouting_profiles.json

Player image: assets/players/rishabh_pant.png

Photograph metadata: data/rishabh_pant_photo_credit.json

## Run Locally

1. Clone the GitHub repository.
2. Open a terminal in the project directory.
3. Install dependencies using:

    python -m pip install -r requirements.txt

4. Start the application using:

    python -m streamlit run app.py

5. Open the local URL displayed by Streamlit.

## Data and Methodology

The project analyzes historical ball-by-ball cricket data
covering IPL, T20I, and other T20 matches.

The published dashboard reads a prepared Excel workbook
containing analytical results.

Player scouting profiles are stored in JSON format.

The application does not require the original Jupyter notebook
or raw ball-by-ball datasets to run.

The methodology includes historical pressure-performance
evaluation, context-adjusted comparisons, and ranking
stability analysis.

The bowling selection includes a documented judgment-based
selection of Varun Chakravarthy. The original model ranking
is preserved rather than presenting the selection as an
automatic model recommendation.

## Important Limitations

- Historical performance does not guarantee future results.
- The analysis is descriptive, not predictive.
- Most identified pressure opportunities occur in death overs.
- Different match contexts may not be equally represented.
- Player availability and contractual status are not verified.
- Auction eligibility and acquisition costs are not established.
- Rankings depend on analytical assumptions.
- Judgment-based selections are distinguished from model rankings.

## Player Photograph Attribution

Player: Rishabh Pant

Photographer: Ben Sutherland from Crystal Palace, London, UK

Original file: Rishabh Pant (29693622367) (cropped).jpg

Source:
https://commons.wikimedia.org/wiki/File:Rishabh_Pant_(29693622367)_(cropped).jpg

License: Creative Commons Attribution 2.0 (CC BY 2.0)

License details:
https://creativecommons.org/licenses/by/2.0/

Modification: Converted from JPEG to PNG.

The photograph is credited to its original photographer.
The project does not claim ownership of the photograph.

## Disclaimer

SupeRR Selector 2027 — RR War Room is an independent
educational cricket analytics project.

It is not officially associated with, sponsored by,
or endorsed by Rajasthan Royals, the IPL, or any
professional cricket organization.
