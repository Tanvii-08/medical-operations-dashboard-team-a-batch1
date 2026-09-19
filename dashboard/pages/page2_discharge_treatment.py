"""
Dashboard Page 2 — Patient Discharge & Flow (Keerthi) + Treatment & Service Demand (Sarthak)
"""

import dash
from dash import html

dash.register_page(__name__, path="/page2", name="Page 2: Discharge & Treatment",order=2,)

layout = html.Div(
    [
        html.H3("Patient Discharge & Flow"),
        html.Iframe(
            src="/assets/reports/discharge_flow.html",
            style={"width": "100%", "height": "1600px", "border": "none"},
        ),
        html.Hr(),
        html.H3("Treatment & Service Demand"),
        html.Iframe(
            src="/assets/reports/treatment_demand.html",
            style={"width": "100%", "height": "900px", "border": "none"},
        ),
    ],
    style={"padding": "24px"},
)
