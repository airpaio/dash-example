import dash_bootstrap_components as dbc
from dash import html

from apps.navbar import navbar


def jumbotron():
    """
    jumbotron is a UI component used to display a large banner type component across the page
    """
    heading = html.Div(
        dbc.Container(
            [
                html.Br(),
                html.Center(html.H2("Welcome to the Dash Example app!!!", className="display-3")),
                html.Center(
                    html.P(
                        "Only folks in the ADMIN group should be able to reach this page!",
                        className="lead"
                    )
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-white rounded-3",
    )
    return heading

def layout():
    """
        layout pieces together the overall page layout
    """
    nav = navbar()
    welcome = jumbotron()
    return html.Div([nav, welcome])