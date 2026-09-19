"""
Medical Operations Intelligence Dashboard — Milestone 4
Main entry point. Run from the REPO ROOT:
    python dashboard/app.py
Then open http://localhost:8050
"""

import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
    [
        html.I(className="fa-solid fa-house-medical", style={"marginRight": "8px"}),
        "MedCore Analytics",
    ],
    className="sidebar-logo",
),
                html.Div(
                    [
                        dcc.Link(page["name"], href=page["path"], className="sidebar-link")
                        for page in dash.page_registry.values()
                    ]
                ),
            ],
            className="sidebar",
        ),
        html.Div(
            dash.page_container,
            className="main-content",
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)