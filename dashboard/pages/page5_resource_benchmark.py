"""
Dashboard Page 5 — Department-wise Resource Utilization (Deepika/team) + Benchmark & Capacity Gap Analysis
"""

import dash
from dash import html

dash.register_page(__name__, path="/page5", name="Page 5: Resources & Benchmarks",order=5,)

layout = html.Div(
    [
        html.H3("Department-wise Resource Utilization"),
        html.Iframe(
            src="/assets/reports/department_resource_utilization.html",
            style={"width": "100%", "height": "1800px", "border": "none"},
        ),
        html.Hr(),
        html.H3("Benchmark & Capacity Gap Analysis"),
        html.Iframe(
            src="/assets/reports/benchmark_capacity_gap.html",
            style={"width": "100%", "height": "1600px", "border": "none"},
        ),
    ],
    style={"padding": "24px"},
)
