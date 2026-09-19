"""
Demo host app for the Patient Flow / Resource Utilization integration.

Shows two ways these pages can be pulled into the real unified
dashboard:

1. Dash Pages (recommended, Dash >= 2.5): set `use_pages=True` and drop
   pages/patient_flow.py + pages/resource_utilization.py straight into
   the main app's `pages/` folder. Dash auto-registers routes
   (see the `dash.register_page(...)` calls at the bottom of each file).

2. Manual mounting: import `get_layout()` from each module and place it
   inside whatever tab/URL routing structure the main app already uses
   (e.g. inside a dcc.Tabs, or a callback keyed off dcc.Location).

This file runs standalone for local testing of just these two pages.
"""

import dash
from dash import Dash, html, dcc, Input, Output

from pages import patient_flow, resource_utilization

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Module 2 & 3 Integration Preview"

NAV_LINKS = [
    ("/patient-flow", "Patient Flow"),
    ("/resource-utilization", "Resource Utilization"),
]

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Nav(
        style={"display": "flex", "gap": "16px", "padding": "12px 20px", "background": "#1f2a44"},
        children=[
            dcc.Link(label, href=href, style={"color": "white", "textDecoration": "none", "fontWeight": "bold"})
            for href, label in NAV_LINKS
        ],
    ),
    html.Div(id="page-content", style={"padding": "20px"}),
])


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def route(pathname):
    if pathname == "/resource-utilization":
        return resource_utilization.get_layout()
    # default: patient flow
    return patient_flow.get_layout()


if __name__ == "__main__":
    import threading
    import webbrowser

    def _open_browser():
        webbrowser.open("http://127.0.0.1:8050")

    # Open the browser automatically ~1 second after the server starts,
    # so anyone running `python app.py` sees the dashboard immediately
    # instead of just the terminal startup message.
    threading.Timer(1.0, _open_browser).start()

    app.run(debug=True, host="0.0.0.0", port=8050, use_reloader=False)
