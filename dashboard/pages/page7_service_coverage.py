import dash
from dash import html

dash.register_page(
    __name__,
    path="/page7",
    name="Page 7: Service Coverage",
    order=7,
)

layout = html.Div([
    html.H2("Healthcare Service Coverage Map"),

    html.Iframe(
        src="/assets/service-coverage-map/index.html",
        style={
            "width": "100%",
            "height": "850px",
            "border": "none"
        }
    )
])