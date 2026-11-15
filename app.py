
import streamlit as st
import pandas as pd
from pathlib import Path
from html import escape

st.set_page_config(
    page_title="SupeRR Selector 2027 | RR War Room",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

PROJECT_DIR = Path(__file__).resolve().parent
EXCEL_PATH = PROJECT_DIR / "SupeRR_Selector_Analysis.xlsx"

@st.cache_data
def load_data():
    batting = pd.read_excel(EXCEL_PATH, sheet_name="Batting Top 10")
    bowling = pd.read_excel(EXCEL_PATH, sheet_name="Bowling Top 10")
    return batting, bowling

batting, bowling = load_data()

def html(content):
    st.markdown(
        content.strip(),
        unsafe_allow_html=True
    )

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');

:root {
    --rr-pink: #e50693;
    --rr-pink-dark: #c2047c;
    --rr-dark: #1b1b27;
    --rr-bg: #f6f6f9;
    --rr-muted: #6f6f82;
    --rr-border: #d9d9e3;
}

html, body, [class*="css"], [data-testid="stAppViewContainer"] {
    font-family: 'Montserrat', sans-serif !important;
}

.stApp {
    background: var(--rr-bg);
    color: var(--rr-dark);
}

.block-container {
    max-width: 1400px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}

[data-testid="stSidebar"],
[data-testid="collapsedControl"] {
    display: none;
}

h1, h2, h3, p {
    font-family: 'Montserrat', sans-serif;
}

.rr-nav {
    background: var(--rr-pink);
    color: white;
    padding: 18px 25px;
    border-radius: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    margin-bottom: 22px;
}

.rr-brand {
    font-size: 18px;
    font-weight: 900;
    letter-spacing: -.5px;
}

.rr-nav-links {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    white-space: nowrap;
}

.rr-hero {
    background: var(--rr-dark);
    color: white;
    padding: 70px 60px;
    border-radius: 8px;
    min-height: 400px;
    position: relative;
    overflow: hidden;
}

.rr-hero::after {
    content: "RR";
    position: absolute;
    right: -20px;
    bottom: -125px;
    font-size: 380px;
    font-weight: 900;
    color: rgba(229,6,147,.13);
    pointer-events: none;
}

.rr-kicker {
    color: var(--rr-pink);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
}

.rr-hero h1 {
    font-size: clamp(42px, 5.5vw, 78px);
    font-weight: 900;
    line-height: 1.02;
    letter-spacing: -3px;
    color: white !important;
    max-width: 850px;
    margin: 24px 0;
}

.rr-hero p {
    color: #e7e7ed;
    max-width: 650px;
    font-size: 15px;
    line-height: 1.8;
}

.rr-accent {
    color: var(--rr-pink);
}

.rr-section {
    margin-top: 55px;
    margin-bottom: 20px;
}

.rr-section-label {
    color: var(--rr-pink);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.rr-section-title {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -1px;
    color: var(--rr-dark);
}

.rr-stat {
    background: white;
    border-top: 4px solid var(--rr-pink);
    padding: 25px 20px;
    border-radius: 5px;
    min-height: 145px;
}

.rr-stat-number {
    font-size: clamp(28px, 3vw, 42px);
    font-weight: 900;
    color: var(--rr-dark);
}

.rr-stat-label {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.3px;
    color: var(--rr-muted);
    margin-top: 10px;
}

.rr-feature {
    background: white;
    border-radius: 5px;
    overflow: hidden;
    border: 1px solid var(--rr-border);
    margin-bottom: 15px;
}

.rr-feature-head {
    background: var(--rr-dark);
    padding: 25px;
    min-height: 155px;
}

.rr-feature-rank {
    font-size: 11px;
    font-weight: 800;
    color: var(--rr-pink);
    letter-spacing: 1.5px;
}

.rr-feature-name {
    color: white;
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.rr-feature-body {
    padding: 25px;
}

.rr-feature-score {
    font-size: 34px;
    font-weight: 900;
    color: var(--rr-pink);
}

.rr-feature-caption {
    font-size: 12px;
    color: var(--rr-muted);
    line-height: 1.8;
    margin-top: 12px;
}

.rr-story {
    background: white;
    border-left: 5px solid var(--rr-pink);
    padding: 30px;
    border-radius: 5px;
    color: var(--rr-dark);
    font-size: 15px;
    line-height: 1.9;
}

.rr-footer {
    margin-top: 60px;
    padding: 24px 0;
    border-top: 1px solid var(--rr-border);
    color: var(--rr-muted);
    font-size: 11px;
}
</style>
""", unsafe_allow_html=True)

# NAVIGATION
html("""
<div class="rr-nav">
  <div class="rr-brand">SUPERR SELECTOR <span style="opacity:.7">/ 2027</span></div>
  <div class="rr-nav-links">WAR ROOM &nbsp; / &nbsp; BATTERS &nbsp; / &nbsp; BOWLERS &nbsp; / &nbsp; ANALYTICS &nbsp; / &nbsp; FINAL XI+</div>
</div>
""")

# HERO
html("""
<div class="rr-hero">
  <div class="rr-kicker">RAJASTHAN ROYALS • SCOUTING INTELLIGENCE</div>
  <h1>BUILT FOR THE<br><span class="rr-accent">MOMENTS</span><br>THAT MATTER.</h1>
  <p>200,999 deliveries. 883 matches. One scouting mission:
  find the batters and bowlers who outperform expectations
  when match situations become demanding.</p>
</div>
""")

# KPI SECTION
html("""
<div class="rr-section">
  <div class="rr-section-label">01 / THE EVIDENCE</div>
  <div class="rr-section-title">THE PRESSURE INDEX</div>
</div>
""")

cols = st.columns(4)

kpis = [
    ("883", "MATCHES ANALYSED"),
    ("200,999", "DELIVERIES STUDIED"),
    ("46,990", "PRESSURE OPPORTUNITIES"),
    (str(len(batting) + len(bowling)), "FINAL PLAYER PICKS")
]

for col, (value, label) in zip(cols, kpis):
    with col:
        html(f"""
<div class="rr-stat">
  <div class="rr-stat-number">{value}</div>
  <div class="rr-stat-label">{label}</div>
</div>
""")

# FEATURED PLAYERS
html("""
<div class="rr-section">
  <div class="rr-section-label">02 / SCOUTING SPOTLIGHT</div>
  <div class="rr-section-title">THE HEADLINERS</div>
</div>
""")

top_batter = batting.sort_values("strict_rank").iloc[0]
top_bowler = bowling.sort_values("proposed_selection_order").iloc[0]

left, right = st.columns(2)

with left:
    html(f"""
<div class="rr-feature">
  <div class="rr-feature-head">
    <div class="rr-feature-rank">01 / TOP BATTING SELECTION</div>
    <div class="rr-feature-name">{escape(str(top_batter['striker_name']))}</div>
  </div>
  <div class="rr-feature-body">
    <div class="rr-feature-score">{top_batter['composite_score']:.2f} / 100</div>
    <div class="rr-feature-caption">
      PRESSURE PERFORMANCE SCORE<br>
      {int(top_batter['pressure_balls'])} pressure balls analysed<br>
      {top_batter['runs_above_expected_per_100_balls']:+.2f}
      runs above expected per 100 balls
    </div>
  </div>
</div>
""")

with right:
    html(f"""
<div class="rr-feature">
  <div class="rr-feature-head">
    <div class="rr-feature-rank">01 / TOP BOWLING SELECTION</div>
    <div class="rr-feature-name">{escape(str(top_bowler['bowler_name']))}</div>
  </div>
  <div class="rr-feature-body">
    <div class="rr-feature-score">{top_bowler['ipl_aware_score']:.2f} / 100</div>
    <div class="rr-feature-caption">
      IPL-AWARE BOWLING SCORE<br>
      {int(top_bowler['ipl_legal_balls'])} IPL pressure legal balls<br>
      {top_bowler['ipl_runs_prevented_per_6']:+.2f}
      runs prevented per six legal balls
    </div>
  </div>
</div>
""")

# STORY
html("""
<div class="rr-section">
  <div class="rr-section-label">03 / THE SCOUTING PHILOSOPHY</div>
  <div class="rr-section-title">BEYOND RUNS. BEYOND WICKETS.</div>
</div>
""")

html("""
<div class="rr-story">
  <strong>Traditional statistics tell us who scores runs and takes wickets.
  We ask who exceeds expectations in demanding match situations.</strong>
  <br><br>
  Our analysis reconstructs match context from ball-by-ball data,
  identifies pressure opportunities, compares players against
  context-adjusted benchmarks, and tests whether the selections
  remain credible across different ranking assumptions.
  <br><br>
  <strong>THE GOAL:</strong> Turn complex cricket analytics into
  clear, evidence-driven scouting recommendations for Rajasthan Royals.
</div>
""")

html("""
<div class="rr-footer">
  SUPERR SELECTOR 2027 • INDEPENDENT RAJASTHAN ROYALS-INSPIRED SCOUTING PROJECT<br>
  Historical descriptive analysis • Not an official Rajasthan Royals product
  • Not a prediction of player availability or future performance
</div>
""")



# ============================================================
# RR_INTERACTIVE_BATTING_CHART_V1
# INTERACTIVE BATTING PRESSURE PERFORMANCE
# ============================================================

import plotly.graph_objects as go

html("""
<div class="rr-section">
  <div class="rr-section-label">04 / BATTING INTELLIGENCE</div>
  <div class="rr-section-title">
    WHO BEATS THE PRESSURE?
  </div>
</div>
""")

st.markdown(
    "### Runs scored above expectation"
)

st.caption(
    "A higher value means the batter scored more runs "
    "than our contextual benchmark expected per 100 pressure balls."
)

chart_df = batting.copy()

chart_df = chart_df.sort_values(
    "runs_above_expected_per_100_balls",
    ascending=True
)

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=chart_df[
            "runs_above_expected_per_100_balls"
        ],
        y=chart_df["striker_name"],
        orientation="h",
        marker=dict(
            color="#E50693"
        ),
        customdata=chart_df[
            [
                "pressure_balls",
                "composite_score",
                "strict_rank"
            ]
        ].to_numpy(),
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Runs above expected / 100: %{x:.2f}<br>"
            "Pressure balls: %{customdata[0]:,.0f}<br>"
            "Overall pressure score: %{customdata[1]:.2f}<br>"
            "Overall selection rank: #%{customdata[2]:.0f}"
            "<extra></extra>"
        ),
        text=chart_df[
            "runs_above_expected_per_100_balls"
        ].round(1),
        textposition="outside"
    )
)

fig.update_layout(
    height=610,
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Montserrat, Arial, sans-serif",
        color="#1B1B27",
        size=14
    ),
    margin=dict(
        l=25,
        r=80,
        t=25,
        b=55
    ),
    xaxis=dict(
        title="Runs above expected per 100 pressure balls",
        title_font=dict(color="#1B1B27", size=14),
        tickfont=dict(color="#1B1B27", size=12),
        showgrid=True,
        gridcolor="#EEEEF2",
        zeroline=False
    ),
    yaxis=dict(
        title="",
        tickfont=dict(
            color="#1B1B27",
            size=15,
            family="Montserrat, Arial, sans-serif"
        ),
        showgrid=False,
        automargin=True
    ),
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

html("""
<div class="rr-story">
  <strong>THE COACH'S TAKEAWAY</strong><br><br>
  This chart shows which selected batters scored the most
  runs above expectation in comparable pressure situations.
  <br><br>
  <strong>Remember:</strong> The highest scoring advantage
  does not automatically mean the highest overall selection
  rank. Our final batting rankings also consider dismissal
  avoidance, consistency, and reliability.
</div>
""")



# ============================================================
# RR_INTERACTIVE_BOWLING_CHART_V1
# IPL BOWLING PRESSURE INTELLIGENCE
# ============================================================

import plotly.graph_objects as go

html("""
<div class="rr-section">
  <div class="rr-section-label">
    05 / IPL BOWLING INTELLIGENCE
  </div>
  <div class="rr-section-title">
    WHO CONTROLS THE GAME UNDER PRESSURE?
  </div>
</div>
""")

st.markdown("### Runs prevented in demanding IPL situations")

st.caption(
    "Positive values mean a bowler conceded fewer runs "
    "than our contextual benchmark expected across "
    "six legal pressure deliveries."
)

# ------------------------------------------------------------
# PREPARE REAL BOWLING DATA
# ------------------------------------------------------------

bowling_chart_df = bowling.copy()

bowling_chart_df = bowling_chart_df.sort_values(
    "ipl_runs_prevented_per_6",
    ascending=True
)

# RR colours
RR_PINK = "#E50693"
RR_DARK = "#1B1B27"

# Positive run prevention = magenta
# Negative run prevention = dark navy
bar_colors = [
    RR_PINK if value >= 0 else RR_DARK
    for value in bowling_chart_df[
        "ipl_runs_prevented_per_6"
    ]
]

# ------------------------------------------------------------
# INTERACTIVE CHART
# ------------------------------------------------------------

fig_bowling = go.Figure()

fig_bowling.add_trace(
    go.Bar(
        x=bowling_chart_df[
            "ipl_runs_prevented_per_6"
        ],

        y=bowling_chart_df["bowler_name"],

        orientation="h",

        selected=dict(
            marker=dict(opacity=1)
        ),
        unselected=dict(
            marker=dict(opacity=1)
        ),

        marker=dict(
            color=bar_colors
        ),

        customdata=bowling_chart_df[
            [
                "ipl_legal_balls",
                "ipl_wickets_per_100",
                "ipl_aware_score",
                "proposed_selection_order",
                "top10_scenarios"
            ]
        ].to_numpy(),

        hovertemplate=(
            "<b>%{y}</b><br>"
            "Runs prevented / 6 balls: %{x:+.2f}<br>"
            "IPL pressure balls: %{customdata[0]:,.0f}<br>"
            "Wickets / 100 balls: %{customdata[1]:.2f}<br>"
            "IPL-aware score: %{customdata[2]:.2f}<br>"
            "Selection position: #%{customdata[3]:.0f}<br>"
            "Top-10 scenarios: %{customdata[4]:.0f}/4"
            "<extra></extra>"
        ),

        text=[
            f"{value:+.2f}"
            for value in bowling_chart_df[
                "ipl_runs_prevented_per_6"
            ]
        ],

        textposition="outside",

        cliponaxis=False
    )
)

# Zero reference line
fig_bowling.add_vline(
    x=0,
    line_width=2,
    line_color="#6F6F82"
)

# ------------------------------------------------------------
# RR WEBSITE-INSPIRED STYLING
# ------------------------------------------------------------

fig_bowling.update_layout(
    height=640,

    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",

    font=dict(
        family="Montserrat, Arial, sans-serif",
        color="#1B1B27",
        size=14
    ),

    margin=dict(
        l=25,
        r=90,
        t=35,
        b=60
    ),

    xaxis=dict(
        title="Runs prevented per six IPL pressure balls",
        title_font=dict(
            color="#1B1B27",
            size=14
        ),
        tickfont=dict(
            color="#1B1B27",
            size=12
        ),
        showgrid=True,
        gridcolor="#EEEEF2",
        zeroline=False
    ),

    yaxis=dict(
        title="",
        tickfont=dict(
            color="#1B1B27",
            size=15,
            family="Montserrat, Arial, sans-serif"
        ),
        showgrid=False,
        automargin=True
    ),

    showlegend=False,
    dragmode=False,

    bargap=0.24
)

st.plotly_chart(
    fig_bowling,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False
    }
)

# ------------------------------------------------------------
# COACH-FRIENDLY EXPLANATION
# ------------------------------------------------------------

html("""
<div class="rr-story">
  <strong>THE COACH'S TAKEAWAY</strong>
  <br><br>

  <strong>Sunil Narine</strong> leads our selected bowlers
  in IPL pressure run prevention, conceding approximately
  3.97 fewer runs than expected per six legal balls.

  <br><br>

  <strong>Rashid Khan</strong> remains our No. 1 overall
  IPL-aware bowling selection because the final scouting
  score combines multiple factors, including run prevention,
  wicket-taking, broader performance, and evidence strength.

  <br><br>

  <strong>Important:</strong> A negative run-prevention value
  means the bowler conceded more runs than the contextual
  benchmark expected. It does not automatically mean the
  bowler is ineffective in every match situation.
</div>
""")




# ============================================================
# RR_BATTING_RELIABILITY_MATRIX_V1
# BATTING PERFORMANCE VS EVIDENCE
# ============================================================

import plotly.express as px

html("""
<div class="rr-section">
    <div class="rr-section-label">
        06 / BATTING RELIABILITY
    </div>
    <div class="rr-section-title">
        PERFORMANCE IS ONE THING. PROVING IT IS ANOTHER.
    </div>
</div>
""")

st.markdown("### The Batting Evidence Matrix")

st.caption(
    "Compare pressure scoring performance with the amount "
    "of ball-by-ball evidence supporting each player."
)

# ------------------------------------------------------------
# PREPARE VERIFIED BATTING DATA
# ------------------------------------------------------------

reliability_df = batting.copy()

reliability_df["player_label"] = reliability_df["striker_name"]

# ------------------------------------------------------------
# CREATE INTERACTIVE SCATTER PLOT
# ------------------------------------------------------------

fig_reliability = px.scatter(
    reliability_df,

    x="runs_above_expected_per_100_balls",
    y="pressure_balls",

    size="composite_score",

    text=None,

    hover_name="striker_name",

    custom_data=[
        "pressure_matches",
        "composite_score",
        "strict_rank"
    ],

    size_max=48
)

fig_reliability.update_traces(
    marker=dict(
        color="#E50693",
        opacity=0.78,
        line=dict(
            color="#1B1B27",
            width=1
        )
    ),

    textposition="top center",

    textfont=dict(
        family="Montserrat, Arial, sans-serif",
        color="#1B1B27",
        size=11
    ),

    hovertemplate=(
        "<b>%{hovertext}</b><br>"
        "Runs above expected / 100: %{x:+.2f}<br>"
        "Pressure balls: %{y:,.0f}<br>"
        "Pressure matches: %{customdata[0]:.0f}<br>"
        "Overall pressure score: %{customdata[1]:.2f}<br>"
        "Overall selection rank: #%{customdata[2]:.0f}"
        "<extra></extra>"
    )
)

# ------------------------------------------------------------
# RR WEBSITE-INSPIRED STYLING
# ------------------------------------------------------------

fig_reliability.update_layout(
    height=660,

    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",

    font=dict(
        family="Montserrat, Arial, sans-serif",
        color="#1B1B27",
        size=13
    ),

    margin=dict(
        l=75,
        r=65,
        t=70,
        b=75
    ),

    xaxis=dict(
        title="Runs above expected per 100 pressure balls",
        title_font=dict(color="#1B1B27", size=13),
        tickfont=dict(color="#1B1B27", size=12),
        gridcolor="#EEEEF2",
        zeroline=False
    ),

    yaxis=dict(
        title="Pressure balls analysed",
        title_font=dict(color="#1B1B27", size=13),
        tickfont=dict(color="#1B1B27", size=12),
        gridcolor="#EEEEF2",
        zeroline=False
    ),

    showlegend=False,

    dragmode=False
)

st.plotly_chart(
    fig_reliability,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False
    }
)

# ------------------------------------------------------------

# COACH-FRIENDLY EXPLANATION

st.markdown("### HOW TO READ THIS CHART")

st.markdown("""
**Further right:** The batter scored more runs above
expectation per 100 pressure balls.

**Higher up:** More pressure deliveries were available
for evaluation.

**Larger bubble:** Higher overall batting composite score.

**THE SCOUTING LESSON**

Strong performance supported by a larger sample is generally
more informative than a similar result from very few deliveries.

However, sample size alone does not establish match-to-match
consistency.

Our final batting rankings also consider dismissal avoidance,
consistency, and reliability.
""")

st.markdown("**PLAYERS INCLUDED IN THIS ANALYSIS**")

player_names = ", ".join(
    batting.sort_values("strict_rank")["striker_name"].tolist()
)

st.caption(player_names)



# ============================================================
# RR_BATTING_CONSISTENCY_V1
# POSITIVE MATCH PERCENTAGE
# ============================================================

import plotly.graph_objects as go

html("""
<div class="rr-section">
  <div class="rr-section-label">
    07 / BATTING CONSISTENCY
  </div>
  <div class="rr-section-title">
    THE RELIABILITY TEST
  </div>
</div>
""")

st.markdown("### Who delivers repeatedly under pressure?")

st.caption(
    "Percentage of meaningful pressure matches classified "
    "as positive by our batting performance model."
)

# ------------------------------------------------------------
# LOAD BATTING STABILITY DATA
# ------------------------------------------------------------

@st.cache_data
def load_batting_stability():
    return pd.read_excel(
        EXCEL_PATH,
        sheet_name="Batting Stability"
    )

stability_df = load_batting_stability()

# Include only our final 10 batting selections
selected_names = batting["striker_name"].tolist()

consistency_df = stability_df[
    stability_df["striker_name"].isin(selected_names)
].copy()

# Confirm every shortlisted player is represented
if len(consistency_df) != 10:
    st.warning(
        f"Expected 10 shortlisted batters, "
        f"but found {len(consistency_df)} records."
    )

# Sort by positive-match percentage
consistency_df = consistency_df.sort_values(
    "positive_match_pct",
    ascending=True
)

# Differentiate the overall No. 1 selection
bar_colors = [
    "#C2047C" if name == "Tim David" else "#E50693"
    for name in consistency_df["striker_name"]
]

# ------------------------------------------------------------
# BUILD INTERACTIVE CHART
# ------------------------------------------------------------

fig_consistency = go.Figure()

fig_consistency.add_trace(
    go.Bar(
        x=consistency_df["positive_match_pct"],

        y=consistency_df["striker_name"],

        orientation="h",

        marker=dict(color=bar_colors),

        customdata=consistency_df[
            [
                "positive_matches",
                "meaningful_matches",
                "pressure_matches",
                "shrunk_consistency",
                "reliability_score"
            ]
        ].to_numpy(),

        text=[
            f"{row.positive_match_pct:.1f}%  "
            f"({int(row.positive_matches)}/"
            f"{int(row.meaningful_matches)})"
            for row in consistency_df.itertuples()
        ],

        textposition="outside",

        cliponaxis=False,

        hovertemplate=(
            "<b>%{y}</b><br>"
            "Positive-match rate: %{x:.1f}%<br>"
            "Positive matches: %{customdata[0]:.0f}<br>"
            "Meaningful matches: %{customdata[1]:.0f}<br>"
            "All pressure matches: %{customdata[2]:.0f}<br>"
            "Smoothed consistency: %{customdata[3]:.3f}<br>"
            "Reliability score: %{customdata[4]:.2f}"
            "<extra></extra>"
        )
    )
)

fig_consistency.update_layout(
    height=650,

    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",

    font=dict(
        family="Montserrat, Arial, sans-serif",
        color="#1B1B27",
        size=14
    ),

    margin=dict(
        l=25,
        r=135,
        t=35,
        b=65
    ),

    xaxis=dict(
        title="Positive meaningful pressure matches (%)",
        range=[0, 105],
        ticksuffix="%",
        showgrid=True,
        gridcolor="#EEEEF2",
        tickfont=dict(
            color="#1B1B27",
            size=12
        )
    ),

    yaxis=dict(
        title="",
        tickfont=dict(
            color="#1B1B27",
            size=14
        ),
        automargin=True,
        showgrid=False
    ),

    bargap=0.27,

    showlegend=False,

    dragmode=False
)

st.plotly_chart(
    fig_consistency,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False
    }
)

# ------------------------------------------------------------
# SCOUTING TAKEAWAYS
# ------------------------------------------------------------

st.markdown("### THE COACH'S TAKEAWAY")

st.markdown("""
**Suryakumar Yadav** has the highest positive-match
percentage among our ten selected batters, with
**23 positive performances in 29 meaningful pressure matches
(79.3%)**.

**Tim David**, our No. 1 overall batting selection,
recorded **30 positive performances across 41 meaningful
pressure matches (73.2%)**.

This illustrates why our scouting model does not rely
on a single statistic. It considers performance,
dismissal avoidance, consistency, and the strength
of supporting evidence.

**Important:** These percentages describe historical
performance in the supplied dataset. They are not
probabilities of success in future IPL matches.
""")




# ============================================================
# RR_BOWLING_STABILITY_HEATMAP_V1
# FOUR-SCENARIO BOWLING RANKING COMPARISON
# ============================================================

import plotly.graph_objects as go

html("""
<div class="rr-section">
    <div class="rr-section-label">
        08 / SCOUTING CONFIDENCE
    </div>
    <div class="rr-section-title">
        THE STABILITY TEST
    </div>
</div>
""")

st.markdown("### Do our bowling picks survive different ranking strategies?")

st.caption(
    "Compare how each selected bowler ranks when "
    "the scouting model prioritises different factors. "
    "A lower rank number is better."
)

# ------------------------------------------------------------
# LOAD VERIFIED IPL BOWLING STABILITY DATA
# ------------------------------------------------------------

@st.cache_data
def load_ipl_bowling_stability():
    return pd.read_excel(
        EXCEL_PATH,
        sheet_name="IPL Bowling Stability"
    )

stability_bowl_df = load_ipl_bowling_stability()

# Preserve the proposed selection order
selected_bowlers = bowling[
    [
        "bowler_name",
        "proposed_selection_order"
    ]
].copy()

heatmap_df = selected_bowlers.merge(
    stability_bowl_df,
    on="bowler_name",
    how="left",
    validate="one_to_one"
)

heatmap_df = heatmap_df.sort_values(
    "proposed_selection_order"
)

# ------------------------------------------------------------
# VERIFY THE DATA
# ------------------------------------------------------------

scenario_columns = [
    "Original_rank",
    "IPL-focused_rank",
    "Wicket-focused_rank",
    "Reliability-focused_rank"
]

if heatmap_df[scenario_columns].isna().any().any():
    st.error(
        "Some selected bowlers are missing scenario rankings."
    )
    st.stop()

scenario_labels = [
    "Original",
    "IPL-focused",
    "Wicket-focused",
    "Reliability-focused"
]

# Actual ranks, one row per bowler
rank_matrix = heatmap_df[
    scenario_columns
].astype(int).to_numpy()

player_names = heatmap_df["bowler_name"].tolist()

# Colour categories:
# 1-3: Elite
# 4-6: Strong
# 7-10: Top 10
# 11+: Outside Top 10

colour_matrix = []

for row in rank_matrix:

    colour_row = []

    for rank in row:

        if rank <= 3:
            colour_row.append(4)

        elif rank <= 6:
            colour_row.append(3)

        elif rank <= 10:
            colour_row.append(2)

        else:
            colour_row.append(1)

    colour_matrix.append(colour_row)

# ------------------------------------------------------------
# BUILD HEATMAP
# ------------------------------------------------------------

fig_stability = go.Figure()

fig_stability.add_trace(
    go.Heatmap(
        z=colour_matrix,

        x=scenario_labels,

        y=player_names,

        text=rank_matrix,

        texttemplate="#%{text}",

        textfont=dict(
            family="Montserrat, Arial, sans-serif",
            size=16
        ),

        colorscale=[
            [0.00, "#F2F2F6"],
            [0.24, "#F2F2F6"],

            [0.25, "#F9C6E4"],
            [0.49, "#F9C6E4"],

            [0.50, "#F04DB1"],
            [0.74, "#F04DB1"],

            [0.75, "#C2047C"],
            [1.00, "#C2047C"]
        ],

        zmin=1,
        zmax=4,

        showscale=False,

        xgap=5,
        ygap=5,

        customdata=rank_matrix,

        hovertemplate=(
            "<b>%{y}</b><br>"
            "Scenario: %{x}<br>"
            "Ranking: #%{customdata}"
            "<extra></extra>"
        )
    )
)

# ------------------------------------------------------------
# RR WEBSITE-INSPIRED STYLING
# ------------------------------------------------------------

fig_stability.update_layout(
    height=670,

    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",

    font=dict(
        family="Montserrat, Arial, sans-serif",
        color="#1B1B27",
        size=14
    ),

    margin=dict(
        l=25,
        r=40,
        t=50,
        b=75
    ),

    xaxis=dict(
        title="Ranking strategy",
        side="bottom",
        tickfont=dict(
            color="#1B1B27",
            size=13
        ),
        showgrid=False
    ),

    yaxis=dict(
        title="",
        autorange="reversed",
        tickfont=dict(
            color="#1B1B27",
            size=14
        ),
        automargin=True,
        showgrid=False
    ),

    dragmode=False
)

st.plotly_chart(
    fig_stability,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False
    }
)

# ------------------------------------------------------------
# SIMPLE LEGEND
# ------------------------------------------------------------

st.markdown(
    "**COLOUR GUIDE:** "
    "🟪 Rank 1–3 (Elite) · "
    "💗 Rank 4–6 (Strong) · "
    "🌸 Rank 7–10 (Top 10) · "
    "⬜ Rank 11+ (Outside Top 10)"
)

# ------------------------------------------------------------
# STABILITY SUMMARY
# ------------------------------------------------------------

fully_stable = int(
    (heatmap_df["top10_scenarios"] == 4).sum()
)

st.markdown("### THE COACH'S TAKEAWAY")

st.markdown(
    f"**{fully_stable} of our 10 selected bowlers** "
    "remain in the top ten across all four "
    "ranking strategies."
)

st.markdown("""
**Rashid Khan** ranks **No. 1 in all four scenarios**,
making him the most stable selection in this analysis.

**Sunil Narine** and **Jasprit Bumrah** also remain
within the top ten under every tested scenario.

**Kuldeep Yadav** appears in the top ten in
three of four scenarios.

**Josh Hazlewood** appears in the top ten in
two of four scenarios. His inclusion as our
proposed tenth selection reflects a scouting
judgment beyond the calculated IPL-aware ranking.

**What this means:** Rankings that remain strong
under different reasonable assumptions provide
more robust historical evidence. This is not
a guarantee of future IPL performance.
""")




# ============================================================


# RR_PLAYER_SCOUTING_VISUAL_FIX_V1

st.markdown("""
<style>

/* Player selector and radio labels */
div[data-testid="stRadio"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stWidgetLabel"] p {
    color: #1B1B27 !important;
    font-weight: 700 !important;
}

/* Scouting statistics */
div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border-top: 3px solid #E50693 !important;
    padding: 18px !important;
    border-radius: 5px !important;
}

/* Metric labels */
div[data-testid="stMetricLabel"] p {
    color: #6F6F82 !important;
    font-weight: 700 !important;
    font-size: 12px !important;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #1B1B27 !important;
    font-weight: 800 !important;
}

/* Radio option text */
div[data-testid="stRadio"] p {
    color: #1B1B27 !important;
}

/* Keep scouting profile text readable */
div[data-testid="stMarkdownContainer"] h3 {
    color: #1B1B27;
}

</style>
""", unsafe_allow_html=True)


# RR_PLAYER_SCOUTING_CENTRE_V1
# INTERACTIVE PLAYER SCOUTING PROFILES
# ============================================================

import html as html_escape
from pathlib import Path

st.markdown("---")

st.markdown(
    '<div class="rr-section-label">'
    '09 / THE SCOUTING CENTRE'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("## MEET THE GAME CHANGERS")

st.caption(
    "Explore the historical pressure-performance evidence "
    "behind our 20 shortlisted players."
)

# RR_SCOUTING_INTELLIGENCE_V1
# Load role-specific scouting profiles from JSON.

import json

_rr_profiles_path = (
    Path(__file__).resolve().parent
    / "data"
    / "player_scouting_profiles.json"
)

with _rr_profiles_path.open(encoding="utf-8") as _rr_file:
    rr_scouting_profiles = json.load(_rr_file)

# ------------------------------------------------------------
# PLAYER SELECTION
# ------------------------------------------------------------

player_category = st.radio(
    "CHOOSE YOUR SCOUTING CATEGORY",
    ["Batters", "Bowlers"],
    horizontal=True,
    key="rr_scout_category"
)

if player_category == "Batters":

    profile_data = batting.sort_values(
        "strict_rank"
    )

    player_column = "striker_name"

else:

    profile_data = bowling.sort_values(
        "proposed_selection_order"
    )

    player_column = "bowler_name"

selected_player = st.selectbox(
    "SELECT A PLAYER",
    profile_data[player_column].tolist(),
    key="rr_scout_player"
)

player_row = profile_data[
    profile_data[player_column] == selected_player
].iloc[0]

# ------------------------------------------------------------
# PLAYER IMAGE
# ------------------------------------------------------------

image_filename = (
    selected_player.lower()
    .replace(" ", "_")
    + ".png"
)

player_image_path = (
    Path(__file__).resolve().parent
    / "assets"
    / "players"
    / image_filename
)

# ------------------------------------------------------------
# PLAYER SPOTLIGHT
# ------------------------------------------------------------

left, right = st.columns([1, 1.6], gap="large")

with left:

    if player_image_path.exists():

        st.image(
            str(player_image_path),
            use_container_width=True
        )

    else:


        # Clean placeholder without nested HTML rendering issues
        safe_name = html_escape.escape(selected_player)

        st.markdown(
            f"""
<div style="
    background:#1B1B27;
    border-top:5px solid #E50693;
    min-height:350px;
    padding:65px 20px;
    text-align:center;
">
    <div style="
        color:#E50693;
        font-size:76px;
        font-weight:900;
        line-height:1;
    ">RR</div>
    <div style="
        color:#FFFFFF;
        font-size:24px;
        font-weight:800;
        margin-top:30px;
    ">{safe_name}</div>
    <div style="
        color:#C8C8D0;
        font-size:12px;
        margin-top:18px;
        letter-spacing:2px;
    ">PLAYER PHOTO COMING SOON</div>
</div>
            """,
            unsafe_allow_html=True
        )

with right:

    if player_category == "Batters":

        selection_rank = int(
            player_row["strict_rank"]
        )

        pressure_score = float(
            player_row["composite_score"]
        )

        scoring_advantage = float(
            player_row[
                "runs_above_expected_per_100_balls"
            ]
        )

        pressure_balls = int(
            player_row["pressure_balls"]
        )

        st.caption(
            f"BATTER / SCOUTING SELECTION #{selection_rank}"
        )

        st.title(selected_player)

        st.metric(
            "OVERALL PRESSURE SCORE",
            f"{pressure_score:.2f} / 100"
        )

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "RUNS ABOVE EXPECTED / 100 BALLS",
                f"{scoring_advantage:+.2f}"
            )

        with c2:
            st.metric(
                "PRESSURE BALLS ANALYSED",
                f"{pressure_balls:,}"
            )

        st.markdown("### THE SCOUTING VERDICT")

        st.write(
            f"{selected_player} scored approximately "
            f"{scoring_advantage:.1f} more runs than "
            "the contextual benchmark expected per "
            "100 pressure balls in the analysed dataset."
        )

        rr_profile = rr_scouting_profiles.get(
            selected_player, {}
        )

        st.markdown("**PLAYER ROLE**")
        st.write(
            rr_profile.get(
                "role",
                "Role requires further scouting assessment."
            )
        )

        st.markdown("**POTENTIAL RR SQUAD VALUE**")
        st.write(
            rr_profile.get(
                "squad_fit",
                "Further squad-fit evaluation required."
            )
        )

        st.markdown("**SCOUTING CAUTION**")
        st.caption(
            rr_profile.get(
                "caution",
                "Historical performance is not a prediction."
            )
        )

    else:

        selection_rank = int(
            player_row["proposed_selection_order"]
        )

        bowling_score = float(
            player_row["ipl_aware_score"]
        )

        run_prevention = float(
            player_row["ipl_runs_prevented_per_6"]
        )

        legal_balls = int(
            player_row["ipl_legal_balls"]
        )

        st.caption(
            f"BOWLER / PROPOSED SELECTION #{selection_rank}"
        )

        st.title(selected_player)

        st.metric(
            "IPL-AWARE SCOUTING SCORE",
            f"{bowling_score:.2f} / 100"
        )

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "RUNS PREVENTED / 6 BALLS",
                f"{run_prevention:+.2f}"
            )

        with c2:
            st.metric(
                "IPL PRESSURE BALLS",
                f"{legal_balls:,}"
            )

        st.markdown("### THE SCOUTING VERDICT")

        if run_prevention >= 0:

            st.write(
                f"{selected_player} conceded approximately "
                f"{run_prevention:.2f} fewer runs than "
                "expected per six legal IPL pressure "
                "deliveries in the analysed dataset."
            )

        else:

            st.write(
                f"{selected_player} conceded approximately "
                f"{abs(run_prevention):.2f} more runs "
                "than expected per six legal IPL pressure "
                "deliveries in the analysed dataset."
            )

        rr_profile = rr_scouting_profiles.get(
            selected_player, {}
        )

        st.markdown("**PLAYER ROLE**")
        st.write(
            rr_profile.get(
                "role",
                "Role requires further scouting assessment."
            )
        )

        st.markdown("**POTENTIAL RR SQUAD VALUE**")
        st.write(
            rr_profile.get(
                "squad_fit",
                "Further squad-fit evaluation required."
            )
        )

        st.markdown("**SCOUTING CAUTION**")
        st.caption(
            rr_profile.get(
                "caution",
                "Historical performance is not a prediction."
            )
        )

        if selected_player == "Josh Hazlewood":

            st.info(
                "Scouting note: Hazlewood is proposed at "
                "selection position #10, although his "
                "calculated IPL-aware rank is #13. "
                "This is a judgment-based inclusion, "
                "not the model's tenth-ranked bowler."
            )

st.caption(
    "Independent historical scouting analysis. "
    "Not an official Rajasthan Royals product, "
    "auction recommendation, or prediction of "
    "future player performance."
)



# RR_SCOUTING_LABEL_CONTRAST_FIX_V1
st.markdown("""
<style>

/* Improve scouting metric label contrast */
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] *,
div[data-testid="stMetric"] label,
div[data-testid="stMetric"] label * {
    color: #505064 !important;
    opacity: 1 !important;
}

/* Keep metric numbers dark and readable */
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] * {
    color: #1B1B27 !important;
}

</style>
""", unsafe_allow_html=True)


# RR_SCOUTING_READABILITY_FIX_V1
# Improve visibility of scouting cautions and disclaimers.

st.markdown(
    """
    <style>

    /* Streamlit caption text */
    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p {
        color: #555568 !important;
        opacity: 1 !important;
    }

    /* General small-text readability */
    .stCaption {
        color: #555568 !important;
        opacity: 1 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# RR_MODEL_METHODOLOGY_V1
# SECTION 10 — BEHIND THE NUMBERS
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="rr-section">
        <div class="rr-section-label">
            10 / BEHIND THE NUMBERS
        </div>
        <div class="rr-section-title">
            THE SCIENCE OF PRESSURE.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "Great scouting starts with asking better questions. "
    "Our model compares player performance against "
    "what similar match situations would typically "
    "demand—not just raw runs or wickets."
)

# ------------------------------------------------------------
# DATA FOUNDATION
# ------------------------------------------------------------

st.markdown("### THE DATA FOUNDATION")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("MATCHES ANALYSED", "883")

with m2:
    st.metric("DELIVERIES ANALYSED", "200,999")

with m3:
    st.metric("PRESSURE OPPORTUNITIES", "46,990")

st.caption(
    "Historical ball-by-ball observations from IPL, "
    "T20I and other T20 cricket, 2022–2026. "
    "Pressure opportunities are a subset of the "
    "recorded deliveries."
)

# ------------------------------------------------------------
# PRESSURE DEFINITION
# ------------------------------------------------------------

st.markdown("### WHAT COUNTS AS PRESSURE?")

st.write(
    "The analysis identifies pressure opportunities "
    "using observable match conditions rather than "
    "trying to measure a player's psychological state."
)

with st.expander(
    "01 / HOW PRESSURE OPPORTUNITIES ARE IDENTIFIED",
    expanded=True
):

    st.markdown(
        """
        **Death overs:** Deliveries during the final
        phase of an innings.

        **Demanding chases:** Situations where the
        required scoring rate creates additional
        batting demands.

        **Competitive close finishes:** Match
        situations identified as closely contested.
        """
    )

    st.warning(
        "Important limitation: approximately 94.6% "
        "of identified pressure opportunities occur "
        "in death overs. The model therefore reflects "
        "death-over performance more strongly than "
        "other forms of match pressure."
    )

# ------------------------------------------------------------
# CONTEXTUAL EXPECTATIONS
# ------------------------------------------------------------

with st.expander(
    "02 / HOW EXPECTED RUNS ARE CALCULATED"
):

    st.write(
        "Actual performance is compared against "
        "smoothed expected runs from comparable "
        "historical match situations."
    )

    st.markdown(
        """
        The contextual baseline considers:

        - Innings
        - Match phase
        - Chase demand
        - Wickets lost

        Smoothing reduces the influence of
        sparsely observed combinations of conditions.
        """
    )

    st.info(
        "A positive batting advantage means a batter "
        "scored more runs than the contextual baseline "
        "expected. Positive bowling run prevention "
        "means a bowler conceded fewer runs than expected."
    )

# ------------------------------------------------------------
# BATTER RANKING
# ------------------------------------------------------------

with st.expander(
    "03 / HOW THE TOP 10 BATTERS ARE SELECTED"
):

    st.markdown(
        """
        **Minimum qualification requirements**

        - 200 pressure balls
        - 20 pressure matches
        - 15 meaningful pressure matches

        **Ranking factors**

        - Context-adjusted scoring
        - Dismissal avoidance
        - Match-to-match consistency
        - Evidence reliability
        """
    )

    st.write(
        "The batting shortlist uses a combined-format "
        "composite score rather than IPL-only performance."
    )

# ------------------------------------------------------------
# BOWLER RANKING
# ------------------------------------------------------------

with st.expander(
    "04 / HOW THE TOP 10 BOWLERS ARE SELECTED"
):

    st.markdown(
        """
        **IPL qualification requirements**

        - 100 IPL pressure legal deliveries
        - 10 IPL pressure matches

        **IPL-aware scoring weights**

        | Component | Weight |
        |---|---:|
        | Overall composite | 50% |
        | IPL run prevention | 25% |
        | IPL wicket-taking | 15% |
        | IPL evidence strength | 10% |
        """
    )

    st.write(
        "This ranking combines broader pressure "
        "performance with IPL-specific evidence."
    )

    st.warning(
        "Josh Hazlewood is proposed at selection "
        "position #10 despite a calculated IPL-aware "
        "rank of #13. His inclusion reflects broader "
        "multi-season IPL scouting judgment, not "
        "the model's tenth-ranked result."
    )

# ------------------------------------------------------------
# ROBUSTNESS
# ------------------------------------------------------------

with st.expander(
    "05 / HOW WE TESTED RANKING STABILITY"
):

    st.write(
        "Player rankings were compared under "
        "alternative scoring priorities to assess "
        "whether the shortlist changes substantially "
        "when model weights change."
    )

    st.markdown(
        """
        The analysis includes scenarios emphasizing:

        - Original model weights
        - Performance or IPL-specific performance
        - Reliability or wicket-taking
        - Alternative balanced priorities
        """
    )

    st.success(
        "Eight of the ten proposed bowlers appeared "
        "in the top ten across all four IPL-aware "
        "ranking scenarios."
    )

# ------------------------------------------------------------
# LIMITATIONS
# ------------------------------------------------------------

with st.expander(
    "06 / WHAT THE MODEL DOES NOT ESTABLISH"
):

    st.markdown(
        """
        This analysis does **not** establish:

        - Player availability for IPL 2027
        - Contract or auction eligibility
        - Acquisition costs
        - Squad composition constraints
        - Future performance
        - Psychological resilience under pressure
        """
    )

    st.write(
        "The results are descriptive historical "
        "indicators intended to support scouting "
        "discussion—not validated predictions "
        "or definitive acquisition recommendations."
    )

st.caption(
    "Methodology documented in the project's "
    "SupeRR Selector Analysis workbook. "
    "Independent analysis; not affiliated with "
    "Rajasthan Royals or the IPL."
)



# ============================================================
# RR_METHODOLOGY_CONTRAST_FIX_V1
# Fix expander headings and notification text contrast
# ============================================================

st.markdown(
    """
    <style>

    /* ---------------------------------------------
       EXPANDER HEADINGS
       --------------------------------------------- */

    [data-testid="stExpander"] details summary,
    [data-testid="stExpander"] details summary p,
    [data-testid="stExpander"] details summary span,
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary p {
        color: #1B1B27 !important;
        opacity: 1 !important;
        -webkit-text-fill-color: #1B1B27 !important;
    }

    /* Expander header background */
    [data-testid="stExpander"] details summary {
        background-color: #F0F0F5 !important;
        border-radius: 6px !important;
    }

    /* ---------------------------------------------
       WARNING BOXES
       --------------------------------------------- */

    [data-testid="stAlert"][data-baseweb="notification"] {
        opacity: 1 !important;
    }

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div {
        color: #1B1B27 !important;
        -webkit-text-fill-color: #1B1B27 !important;
        opacity: 1 !important;
    }

    /* ---------------------------------------------
       EXPANDER CONTENT
       --------------------------------------------- */

    [data-testid="stExpander"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stExpander"] [data-testid="stMarkdownContainer"] li {
        color: #1B1B27 !important;
        opacity: 1 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)
