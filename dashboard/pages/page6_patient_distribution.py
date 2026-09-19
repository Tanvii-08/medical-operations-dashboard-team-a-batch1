import dash
from dash import html

dash.register_page(
    __name__,
    path="/page6",
    name="Page 6: Patient Distribution",
    order=6,
)

layout = html.Div([
    html.H2("Patient Distribution Map"),

    html.Iframe(
        src="/assets/reports/patient_distribution_map.html",
        style={
            "width": "100%",
            "height": "800px",
            "border": "none"
        }
    )
])