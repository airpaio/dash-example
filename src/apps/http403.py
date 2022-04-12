from dash import html
from apps.navbar import navbar


def error_layout():
    """
    error_layout defines a simple layout for unauthorized access
    """
    e_layout = html.Div(
        [
            html.Br(),
            html.Center(html.H2("403 - Forbidden")),
            html.Br(),
            html.Center(html.H4("You're not authorized to do that!!!")),
        ]
    )
    return e_layout

def layout():
    """
    layout pieces together the overall page layout
    """
    nav = navbar()
    e_layout = error_layout()
    return html.Div([nav, e_layout])