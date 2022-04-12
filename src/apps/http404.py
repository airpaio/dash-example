from dash import html
from apps.navbar import navbar


def error_layout():
    """
    error_layout defines a simple layout for unauthorized access
    """
    e_layout = html.Div(
        [
            html.Br(),
            html.Center(html.H2("404 - Not Found")),
            html.Br(),
            html.Center(html.H4("We couldn't find the page you're looking for.")),
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