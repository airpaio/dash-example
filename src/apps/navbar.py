import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State

from app import dash_app

def navbar():
    """
    navbar is a top navigation bar that can be displayed on all pages
    """
    nav_item = dbc.NavItem(
        dbc.NavLink("QuickLink", href="#")
    )

    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Home", href="/"),
            dbc.DropdownMenuItem("Admin", href="/admin"),
            dbc.DropdownMenuItem("Not Admin", href="/notadmin"),
        ],
        nav=True,
        in_navbar=True,
        label="Menu",
    )

    # logo = "assets/dash-example.png"

    navbar_html = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            # dbc.Col(html.H1(html.Img(src=logo, height="40px"))),
                            dbc.Col(
                                dbc.NavbarBrand("Dash Example", className="ms-2")
                            ),
                        ],
                        align="center",
                        className="g=0",
                    ),
                    href="/",
                    style={"textDecoration": "none"}
                ),
                dbc.NavbarToggler(id="navbar-toggler-2", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [nav_item, dropdown],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse-2",
                    navbar=True,
                ),
            ]
        ),
        color="light",
    )
    return navbar_html


@dash_app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    """
    toggle_navbar_collapse controls whether the navbar-collapse dropdown menu is open or closed
    """
    if n:
        return not is_open
    return is_open