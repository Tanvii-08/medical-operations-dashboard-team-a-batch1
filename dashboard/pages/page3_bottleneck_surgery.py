"""
Dashboard Page 3 — Bottlenecks & Capacity Strain (Sarthak) + Surgery Workload (Divya)
"""

import dash
from dash import html

dash.register_page(__name__, path="/page3", name="Page 3: Bottlenecks & Surgery",order=3,)

layout = html.Div(
    [
        html.H3("Bottlenecks & Capacity Strain"),
        html.Iframe(
            src="/assets/reports/bottleneck_capacity.html",
            style={"width": "100%", "height": "1600px", "border": "none"},
        ),
        html.Hr(),
        html.H3("Surgery Workload"),
        html.Iframe(
            src="/assets/reports/surgery_workload.html",
            style={"width": "100%", "height": "2400px", "border": "none"},
        ),
    ],
    style={"padding": "24px"},
)
