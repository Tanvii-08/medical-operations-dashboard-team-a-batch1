import os
import pandas as pd
import dash
from dash import html

dash.register_page(
    __name__,
    path="/",
    name="Executive Overview",
    order=0,
)

ADMISSIONS_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "milestone3",
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

def get_current_admissions():
    if not os.path.exists(ADMISSIONS_PATH):
        return 0

    df = pd.read_csv(ADMISSIONS_PATH)
    if df.empty:
        return 0

    if "admission_date" in df.columns:
        df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce")
        df = df.dropna(subset=["admission_date"])

    return int(len(df))

def get_summary_stats():
    if not os.path.exists(ADMISSIONS_PATH):
        return {
            "currently_admitted": 0,
            "bed_utilization": "N/A",
            "workforce": "N/A",
            "capacity_gaps": "N/A",
        }

    df = pd.read_csv(ADMISSIONS_PATH)
    total = int(len(df)) if not df.empty else 0

    return {
        "currently_admitted": total,
        "bed_utilization": "Page 4",
        "workforce": "Page 4",
        "capacity_gaps": "Page 5",
    }

def build_layout():
    stats = get_summary_stats()

    return html.Div(
        [
            html.H1(
                "Healthcare Operations Intelligence Dashboard",
                style={
                    "fontSize": "28px",
                    "fontWeight": "700",
                    "color": "#0F172A",
                    "marginBottom": "10px",
                },
            ),
            html.Div(
                "Executive Overview | Decision Support",
                style={"fontSize": "18px", "color": "#64748B", "marginBottom": "24px"},
            ),

            html.H2(
                "Executive Snapshot",
                style={
                    "fontSize": "28px",
                    "fontWeight": "700",
                    "color": "#0F172A",
                    "marginBottom": "16px",
                },
            ),

            html.Div(
                [
                    kpi_card(
                        "CURRENTLY ADMITTED",
                        format_kpi(stats["currently_admitted"]),
                        "Active patients as of latest data",
                        icon="fa-bed",
                        color="#0F172A",
                    ),
                    kpi_card(
                        "BED UTILIZATION",
                        str(stats["bed_utilization"]),
                        "Department occupancy analysis",
                        icon="fa-bed",
                        color="#0F172A",
                    ),
                    kpi_card(
                        "WORKFORCE",
                        str(stats["workforce"]),
                        "Staffing efficiency analysis",
                        icon="fa-user-doctor",
                        color="#0F172A",
                    ),
                    kpi_card(
                        "CAPACITY GAPS",
                        str(stats["capacity_gaps"]),
                        "Benchmark comparison",
                        icon="fa-chart-line",
                        color="#0F172A",
                    ),
                ],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(4, minmax(0, 1fr))",
                    "gap": "16px",
                    "marginBottom": "24px",
                },
            ),

            html.Div(
                [
                    html.H3(
                        "Operational Overview",
                        style={
                            "fontSize": "22px",
                            "fontWeight": "700",
                            "color": "#0F172A",
                            "marginBottom": "12px",
                        },
                    ),
                    html.Div(
                        "This executive view brings together the major healthcare operations areas analyzed across the dashboard. Management can use the detailed pages to review patient flow, discharge and treatment demand, operational bottlenecks, workforce utilization, and resource capacity gaps.",
                        style={
                            "fontSize": "18px",
                            "color": "#334155",
                            "backgroundColor": "#F8FAFC",
                            "padding": "20px 24px",
                            "borderRadius": "12px",
                            "border": "1px solid #E2E8F0",
                        },
                    ),
                ],
                style={"marginBottom": "24px"},
            ),

            html.H3(
                "Detailed Operational Views",
                style={
                    "fontSize": "22px",
                    "fontWeight": "700",
                    "color": "#0F172A",
                    "marginBottom": "16px",
                },
            ),

            html.Div(
                [
                    kpi_card("Patient Flow", "Admissions and department patient load", "Patient flow overview", icon="fa-stethoscope", color="#0F172A"),
                    kpi_card("Discharge & Treatment", "Discharge flow and treatment demand", "Discharge and treatment demand", icon="fa-hospital-user", color="#0F172A"),
                    kpi_card("Bottlenecks & Surgery", "Operational bottlenecks and surgery workload", "Surgery and bottlenecks", icon="fa-user-nurse", color="#0F172A"),
                ],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(3, minmax(0, 1fr))",
                    "gap": "16px",
                },
            ),
        ],
        style={"padding": "24px", "backgroundColor": "#F8FAFC", "minHeight": "100vh"},
    )

layout = build_layout()