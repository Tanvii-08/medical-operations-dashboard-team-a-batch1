import os
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "processed",
    "admissions_clean.csv",
)

def format_kpi(value):
    if value is None or pd.isna(value):
        return "0"
    return f"{int(float(value)):,}"

def kpi_card(title, value, description, icon="fa-chart-simple", color="#0F172A"):
    return html.Div(
        [
            html.I(
                className=f"fa-solid {icon}",
                style={"fontSize": "20px", "color": color, "marginBottom": "10px"},
            ),
            html.Div(
                title,
                style={
                    "fontSize": "11px",
                    "letterSpacing": "0.08em",
                    "textTransform": "uppercase",
                    "color": "#64748B",
                },
            ),
            html.Div(
                value,
                style={
                    "fontSize": "28px",
                    "fontWeight": "700",
                    "color": color,
                    "marginTop": "6px",
                },
            ),
            html.Div(
                description,
                style={"fontSize": "12px", "color": "#64748B", "marginTop": "8px"},
            ),
        ],
        style={
            "backgroundColor": "#FFFFFF",
            "borderRadius": "12px",
            "padding": "18px 16px",
            "boxShadow": "0 4px 12px rgba(15, 23, 42, 0.06)",
            "border": "1px solid #E2E8F0",
            "minHeight": "150px",
        },
    )

def load_admissions_data():
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame()

    df = pd.read_csv(DATA_PATH)
    df["Admission_Date"] = pd.to_datetime(df["Admission_Date"], errors="coerce")
    df["Admission_Month_Year"] = df["Admission_Date"].dt.to_period("M").astype(str)

    monthly = (
        df.groupby("Admission_Month_Year")["Admission_ID"]
        .nunique()
        .reset_index(name="Admission_Count")
        .sort_values("Admission_Month_Year")
    )

    monthly["Admission_Month_Year"] = pd.to_datetime(monthly["Admission_Month_Year"], format="%Y-%m")
    return monthly

def make_figure(filtered_df):
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

def admissions_section():
    monthly_admissions = load_admissions_data()

    if monthly_admissions.empty:
        total_admissions = 0
        avg_per_month = 0
        peak_label = "N/A"
        peak_value = 0
        low_label = "N/A"
        low_value = 0
    else:
        total_admissions = int(monthly_admissions["Admission_Count"].sum())
        avg_per_month = int(monthly_admissions["Admission_Count"].mean())
        peak_row = monthly_admissions.loc[monthly_admissions["Admission_Count"].idxmax()]
        low_row = monthly_admissions.loc[monthly_admissions["Admission_Count"].idxmin()]
        peak_label = peak_row["Admission_Month_Year"].strftime("%b %Y")
        peak_value = int(peak_row["Admission_Count"])
        low_label = low_row["Admission_Month_Year"].strftime("%b %Y")
        low_value = int(low_row["Admission_Count"])

    return html.Div(
        [
            html.H1(
                "Admission Trends",
                style={
                    "fontSize": "26px",
                    "fontWeight": "700",
                    "color": "#0F172A",
                    "marginBottom": "18px",
                },
            ),
            html.Div(
                [
                    kpi_card("Total Admissions", format_kpi(total_admissions), "Actual patient admissions", icon="fa-hospital-user", color="#0F172A"),
                    kpi_card("Avg / Month", format_kpi(avg_per_month), "Average monthly admissions", icon="fa-calendar-alt", color="#0F172A"),
                    kpi_card("Peak Month", f"{peak_label} ({format_kpi(peak_value)})", "Highest monthly admissions", icon="fa-arrow-trend-up", color="#0F172A"),
                    kpi_card("Lowest Month", f"{low_label} ({format_kpi(low_value)})", "Lowest monthly admissions", icon="fa-arrow-trend-down", color="#0F172A"),
                ],
                style={"display": "grid", "gridTemplateColumns": "repeat(4, minmax(0, 1fr))", "gap": "16px", "marginBottom": "24px"},
            ),
            html.Div(
                dcc.RangeSlider(
                    id="month-range",
                    min=0,
                    max=len(monthly_admissions) - 1 if not monthly_admissions.empty else 0,
                    step=1,
                    value=[0, len(monthly_admissions) - 1] if not monthly_admissions.empty else [0, 0],
                    marks={i: d.strftime("%b'%y") for i, d in enumerate(monthly_admissions["Admission_Month_Year"])} if not monthly_admissions.empty else {},
                ),
                style={"marginBottom": "20px"},
            ),
            dcc.Graph(
                id="admission-chart",
                figure=make_figure(monthly_admissions) if not monthly_admissions.empty else go.Figure(),
            ),
        ],
        style={"padding": "20px"},
    )