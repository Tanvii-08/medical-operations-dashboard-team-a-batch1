"""
Workforce & Staffing Efficiency — Visualization component (Sarthak)
Registered as part of Page 4 alongside Bed Utilization & Occupancy.
Converted from a standalone Dash app into a multi-page component:
own Dash() instance removed, callback IDs namespaced, app.run() removed.
"""

import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, callback

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
dashboard_df = pd.read_csv("data/processed/workforce_staffing_efficiency.csv")

dashboard_df["Admissions"] = pd.to_numeric(dashboard_df["Admissions"])
dashboard_df["Total_Staff"] = pd.to_numeric(dashboard_df["Total_Staff"])
dashboard_df["Staff_Share_Percent"] = pd.to_numeric(dashboard_df["Staff_Share_Percent"])
dashboard_df["Patients_per_Staff"] = pd.to_numeric(dashboard_df["Patients_per_Staff"])

# ---------------------------------------------------------------------------
# 2. Layout piece — namespaced IDs (prefixed with "wf-") to avoid collisions
#    with other pages' components
# ---------------------------------------------------------------------------
workforce_section = html.Div(
    [
        html.H3("Workforce & Staffing Efficiency"),
        html.P(
            "Department-level staffing workload and resource distribution",
            style={"color": "#6B7280", "fontSize": "14px", "marginTop": "-8px"},
        ),

        html.Div(
            [
                html.Label("Department", style={"fontWeight": "bold", "fontSize": "13px", "color": "#4B5563"}),
                dcc.Dropdown(
                    id="wf-department-filter",
                    options=[{"label": "All Departments", "value": "All Departments"}]
                    + [
                        {"label": dept, "value": dept}
                        for dept in sorted(dashboard_df["department_name"].unique())
                    ],
                    value="All Departments",
                    clearable=False,
                    style={"maxWidth": "300px", "marginBottom": "16px"},
                ),
            ]
        ),

        html.Div(
            style={"display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "14px", "marginBottom": "18px"},
            children=[
                html.Div(
                    [
                        html.P("TOTAL STAFF", style={"fontSize": "12px", "color": "#6B7280", "margin": "0"}),
                        html.H2(id="wf-kpi-staff", style={"color": "#2F5597", "margin": "8px 0 0 0"}),
                    ],
                    style={"backgroundColor": "white", "padding": "18px", "borderRadius": "10px",
                           "borderLeft": "5px solid #2F5597", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"},
                ),
                html.Div(
                    [
                        html.P("TOTAL ADMISSIONS", style={"fontSize": "12px", "color": "#6B7280", "margin": "0"}),
                        html.H2(id="wf-kpi-admissions", style={"color": "#E67E22", "margin": "8px 0 0 0"}),
                    ],
                    style={"backgroundColor": "white", "padding": "18px", "borderRadius": "10px",
                           "borderLeft": "5px solid #E67E22", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"},
                ),
                html.Div(
                    [
                        html.P("PATIENTS / STAFF", style={"fontSize": "12px", "color": "#6B7280", "margin": "0"}),
                        html.H2(id="wf-kpi-ratio", style={"color": "#16A085", "margin": "8px 0 0 0"}),
                    ],
                    style={"backgroundColor": "white", "padding": "18px", "borderRadius": "10px",
                           "borderLeft": "5px solid #16A085", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"},
                ),
                html.Div(
                    [
                        html.P("HIGHEST PRESSURE", style={"fontSize": "12px", "color": "#6B7280", "margin": "0"}),
                        html.H2(id="wf-kpi-pressure", style={"color": "#8E44AD", "margin": "8px 0 0 0", "fontSize": "20px"}),
                        html.P(id="wf-kpi-pressure-value", style={"margin": "3px 0 0 0", "fontSize": "12px", "color": "#6B7280"}),
                    ],
                    style={"backgroundColor": "white", "padding": "18px", "borderRadius": "10px",
                           "borderLeft": "5px solid #8E44AD", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"},
                ),
            ],
        ),

        html.Div(
            style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "18px", "marginBottom": "18px"},
            children=[
                dcc.Graph(id="wf-patients-staff-chart"),
                dcc.Graph(id="wf-staff-distribution-chart"),
            ],
        ),
        html.Div(
            style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "18px"},
            children=[
                dcc.Graph(id="wf-staff-share-chart"),
                dcc.Graph(id="wf-admissions-staff-chart"),
            ],
        ),
    ],
    style={"marginBottom": "40px"},
)


# ---------------------------------------------------------------------------
# 3. Callback — namespaced IDs, same logic as the original Dash app
# ---------------------------------------------------------------------------
@callback(
    Output("wf-kpi-staff", "children"),
    Output("wf-kpi-admissions", "children"),
    Output("wf-kpi-ratio", "children"),
    Output("wf-kpi-pressure", "children"),
    Output("wf-kpi-pressure-value", "children"),
    Output("wf-patients-staff-chart", "figure"),
    Output("wf-staff-distribution-chart", "figure"),
    Output("wf-staff-share-chart", "figure"),
    Output("wf-admissions-staff-chart", "figure"),
    Input("wf-department-filter", "value"),
)
def update_workforce_dashboard(selected_department):
    if selected_department == "All Departments":
        filtered = dashboard_df.copy()
    else:
        filtered = dashboard_df[dashboard_df["department_name"] == selected_department].copy()

    total_staff = filtered["Total_Staff"].sum()
    total_admissions = filtered["Admissions"].sum()
    patients_per_staff = (total_admissions / total_staff) if total_staff > 0 else 0

    highest_row = filtered.loc[filtered["Patients_per_Staff"].idxmax()]
    highest_department = highest_row["department_name"]
    highest_value = highest_row["Patients_per_Staff"]

    chart1_df = filtered.sort_values("Patients_per_Staff", ascending=True)
    fig1 = px.bar(chart1_df, x="Patients_per_Staff", y="department_name", orientation="h",
                  text="Patients_per_Staff",
                  labels={"Patients_per_Staff": "Patients per Staff", "department_name": "Department"},
                  title="Patients per Staff by Department")
    fig1.update_traces(marker_color="#E67E22", texttemplate="%{text:.2f}", textposition="outside")
    fig1.update_layout(title_x=0.5, height=420, margin=dict(l=20, r=30, t=60, b=40),
                        plot_bgcolor="white", paper_bgcolor="white")

    chart2_df = filtered.sort_values("Total_Staff", ascending=False)
    fig2 = px.bar(chart2_df, x="department_name", y="Total_Staff", text="Total_Staff",
                  labels={"department_name": "Department", "Total_Staff": "Total Staff"},
                  title="Staff Distribution Across Departments")
    fig2.update_traces(marker_color="#2F5597", textposition="outside")
    fig2.update_layout(title_x=0.5, height=420, xaxis_tickangle=-45,
                        margin=dict(l=40, r=30, t=60, b=100), plot_bgcolor="white", paper_bgcolor="white")

    fig3 = px.pie(filtered, names="department_name", values="Total_Staff", hole=0.55,
                  title="Staff Share by Department")
    fig3.update_traces(textposition="inside", textinfo="percent",
                        marker=dict(line=dict(color="white", width=1)))
    fig3.update_layout(title_x=0.5, height=420, margin=dict(l=20, r=20, t=60, b=30), paper_bgcolor="white")

    fig4 = px.scatter(filtered, x="Total_Staff", y="Admissions", size="Patients_per_Staff",
                       hover_name="department_name",
                       hover_data={"Total_Staff": True, "Admissions": True,
                                   "Patients_per_Staff": ":.2f", "Staff_Share_Percent": ":.2f"},
                       labels={"Total_Staff": "Total Staff", "Admissions": "Admissions"},
                       title="Admissions vs Total Staff")
    fig4.update_traces(marker=dict(color="#16A085", line=dict(width=1)))
    fig4.update_layout(title_x=0.5, height=420, margin=dict(l=50, r=30, t=60, b=50),
                        plot_bgcolor="white", paper_bgcolor="white")

    return (
        f"{total_staff:,.0f}",
        f"{total_admissions:,.0f}",
        f"{patients_per_staff:.2f}",
        highest_department,
        f"{highest_value:.2f} patients/staff",
        fig1, fig2, fig3, fig4,
    )
