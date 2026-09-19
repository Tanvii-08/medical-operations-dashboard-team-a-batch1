import os
import sys
import dash
from dash import html

BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from page1_admissions_component import admissions_section

dash.register_page(
    __name__,
    path="/page1",
    name="Page 1: Patient Flow",
    order=1,
)

layout = html.Div(
    [
        admissions_section(),
        html.Hr(),
        html.H3("Department-wise Patient Load"),
        html.Iframe(
            src="/assets/reports/dept_load.html",
            style={"width": "100%", "height": "1400px", "border": "none"},
        ),
    ],
    style={"padding": "24px"},
)