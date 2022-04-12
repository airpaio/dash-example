import asyncio
import os
from flask import g
from dash import dcc, html
from dash.dependencies import Input, Output

from app import app, dash_app #, oidc, okta_client
from apps import home, admin, notadmin, http403, http404



def serve_layout():
    """serve_layout will serve the contents and layout of the app
    """
    return html.Div([dcc.Location(id="url", refresh=True), html.Div(id="page-content")])

def protect_views(d_app):
    """
    protect_views ensures that the visitor is authn/authz to view the pages
    """
    for view_func in d_app.server.view_functions:
        if view_func == d_app.server.config["url_base_pathname"]:
            d_app.server.view_functions[view_func] = oidc.require_login(
                d_app.server.view_functions[view_func]
            )
    return d_app


# @app.before_request
# async def before_request():
#     """
#     before_request is executed before the http request to visit the web app is served

#     If the user is loggedin to Okta, then we need to fetch the user's Okta groups
#     """
#     if oidc.user_loggedin:
#         okta_id = g.oidc_id_token["sub"]
#         user_groups, resp, err = await okta_client.list_user_groups(okta_id)
#         if err:
#             print(err)
#         g.groups = parse_user_groups(user_groups)
    
def parse_user_groups(user_groups):
    """
    parse_user_groups will get only Okta group names from the okta_client.list_user_groups response
    """
    groups = []
    for obj in user_groups:
        groups.append(obj.profile.name)
    return groups

def validate_user_groups(authz_groups):
    """
    validate_user_groups will check that the loggedin user is in an appropriate Okta group
    """
    return True # any(group in authz_groups for group in g.groups)

def serve_page(layout, authz_groups):
    """
    serve_page will return the layout of the web page to be served to the authorized groups
    """
    if validate_user_groups(authz_groups):
        return layout
    return http403.layout()

@dash_app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    """
    display_page handles your multi-page dash app routing
    """
    dash_app.server.config["url_base_pathname"] = pathname
    # protect_views(dash_app)

    if pathname == "/":
        page_layout = home.layout()
        authorized_groups = [
            "Dash_Example_ADMIN",
            "Dash_Example_NOT_ADMIN",
        ]
    elif pathname == "/admin":
        page_layout = admin.layout()
        authorized_groups = [
            "Dash_Example_ADMIN",
        ]
    elif pathname == "/notadmin":
        page_layout = notadmin.layout()
        authorized_groups = [
            "Dash_Example_ADMIN",
            "Dash_Example_NOT_ADMIN",
        ]
    else:
        page_layout = http404.layout()
        authorized_groups = [
            "Dash_Example_ADMIN",
            "Dash_Example_NOT_ADMIN",
        ]
    
    layout = serve_page(page_layout, authorized_groups)
    return layout

dash_app.layout = serve_layout

if __name__ == "__main__":
    dash_app.run_server(debug=True, host="0.0.0.0", port=5000)
