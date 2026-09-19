"""
Dashboard Page 4 — Bed Utilization & Occupancy (Tanvi) + Workforce & Staffing Efficiency (Sarthak)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import dash
from dash import html
from page4_workforce_component import workforce_section

dash.register_page(__name__, path="/page4", name="Page 4: Bed & Workforce",order=4,)

layout = html.Div(
    [
        html.H3("Bed Utilization & Occupancy"),
        html.Iframe(
            src="/assets/reports/bed_utilization.html",
            style={"width": "100%", "height": "1050px", "border": "none"},
        ),
        html.Hr(),
        workforce_section,
    ],
    style={"padding": "24px"},
)
