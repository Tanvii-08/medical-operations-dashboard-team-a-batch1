"""
Admission Trends — Visualization + Dashboard Build
Member 2 | Milestone 2 | Medical Operations Intelligence Dashboard

Paired with Member 1's Admission Trends analysis.
Reads from the shared, merged dataset: data/processed/admissions_clean.csv

Run from the REPO ROOT (not from inside dashboard/):
    python dashboard/page1_admissions.py
Then open http://localhost:8050
"""

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

def format_kpi(value):
    if value is None or pd.isna(value):
        return "0"
    return f"{int(float(value)):,}"

# ---------------------------------------------------------------------------
# 1. Load and prep data
# ---------------------------------------------------------------------------
df = pd.read_csv("data/processed/admissions_clean.csv")
df["Admission_Date"] = pd.to_datetime(df["Admission_Date"], errors="coerce")
df["Admission_Month_Year"] = df["Admission_Date"].dt.to_period("M").astype(str)

monthly_admissions = (
    df.groupby("Admission_Month_Year")["Admission_ID"]
    .nunique()
    .reset_index(name="Admission_Count")
    .sort_values("Admission_Month_Year")
)

monthly_admissions["Admission_Month_Year"] = pd.to_datetime(
    monthly_admissions["Admission_Month_Year"], format="%Y-%m"
)

# ---------------------------------------------------------------------------
# 2. KPIs
# ---------------------------------------------------------------------------
total_admissions = int(df["Admission_ID"].nunique())
avg_per_month = int(monthly_admissions["Admission_Count"].mean())
peak_row = monthly_admissions.loc[monthly_admissions["Admission_Count"].idxmax()]
low_row = monthly_admissions.loc[monthly_admissions["Admission_Count"].idxmin()]

# ---------------------------------------------------------------------------
# 3. Chart builder
# ---------------------------------------------------------------------------
def make_figure(filtered_df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=filtered_df["Admission_Month_Year"],
            y=filtered_df["Admission_Count"],
            mode="lines+markers",
            fill="tozeroy",
            line=dict(width=3),
            name="Admissions",
            hovertemplate="%{x|%b %Y}<br>Admissions: %{y}<extra></extra>",
        )
    )
    fig.update_layout(
        title="Monthly Admission Trend",
        xaxis_title="Month",
        yaxis_title="Number of Admissions",
        template="plotly_white",
        margin=dict(l=40, r=20, t=50, b=40),
    )
    return fig

# ---------------------------------------------------------------------------
# 4. KPI cards
# ---------------------------------------------------------------------------
def kpi_card(label: str, value) -> html.Div:
    return html.Div(
        [
            html.Div(label, style={"fontSize": "13px", "color": "#666"}),
            html.Div(str(value), style={"fontSize": "26px", "fontWeight": "700", "color": "#222222"}),
        ],
        style={
            "padding": "16px",
            "borderRadius": "10px",
            "background": "#f5f5f7",
            "textAlign": "center",
            "minWidth": "150px",
        },
    )

kpi_row = html.Div(
    [
        kpi_card("Total Admissions", format_kpi(total_admissions)),
        kpi_card("Avg / Month", format_kpi(avg_per_month)),
        kpi_card(
            "Peak Month",
            f"{peak_row['Admission_Month_Year'].strftime('%b %Y')} ({int(peak_row['Admission_Count'])})",
        ),
        kpi_card(
            "Lowest Month",
            f"{low_row['Admission_Month_Year'].strftime('%b %Y')} ({int(low_row['Admission_Count'])})",
        ),
    ],
    style={"display": "flex", "gap": "16px", "marginBottom": "20px", "flexWrap": "wrap"},
)

# ---------------------------------------------------------------------------
# 5. Date-range filter
# ---------------------------------------------------------------------------
range_slider = dcc.RangeSlider(
    id="month-range",
    min=0,
    max=len(monthly_admissions) - 1,
    step=1,
    value=[0, len(monthly_admissions) - 1],
    marks={i: d.strftime("%b'%y") for i, d in enumerate(monthly_admissions["Admission_Month_Year"])},
)

# ---------------------------------------------------------------------------
# 6. Layout
# ---------------------------------------------------------------------------
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("Admission Trends"),
        kpi_row,
        html.Div(range_slider, style={"marginBottom": "24px", "padding": "0 12px"}),
        dcc.Graph(id="admission-chart", figure=make_figure(monthly_admissions)),
    ],
    style={"padding": "24px", "fontFamily": "Arial, sans-serif"},
)

# ---------------------------------------------------------------------------
# 7. Callback — slider filters the chart
# ---------------------------------------------------------------------------
@app.callback(Output("admission-chart", "figure"), Input("month-range", "value"))
def update_chart(rng):
    sliced = monthly_admissions.iloc[rng[0] : rng[1] + 1]
    return make_figure(sliced)

if __name__ == "__main__":
    app.run(debug=True)