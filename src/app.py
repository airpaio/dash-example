import hashlib
import json
import os

from flask import Flask

from flask_oidc import OpenIDConnect
import dash
import dash_bootstrap_components as dbc

from okta.client import Client as OktaClient

app = Flask(__name__)

# okta_secrets = json.loads(json.loads(os.getenv("OKTA_SECRETS")))
# okta_api = okta_secrets["api"]
# okta_client_id = okta_secrets["client_id"]
# okta_client_secret = okta_secrets["client_secret"]

# DOMAIN = os.getenv("DOMAIN")
# SECRETS_FILE = "client_secrets.json"
# OKTA_DOMAIN = ""

# client_secrets = {
#     "web": {
#         "token_uri": f"{OKTA_DOMAIN}/oauth2/v1/token",
#         "auth_uri": f"{OKTA_DOMAIN}/oauth2/v1/authorize",
#         "client_id": okta_client_id,
#         "client_secret": okta_client_secret,
#         "redirect_uris": [f"{DOMAIN}/oidc/callback"],
#         "userinfo_uri": f"{OKTA_DOMAIN}/oauth2/userinfo",
#         "issuer": f"{OKTA_DOMAIN}/oauth2"
#     }
# }

# with open(SECRETS_FILE, "w", encoding="utf8") as outfile:
#     json.dump(client_secrets, outfile, indent=4)

# app.config["OIDC_CLIENT_SECRETS"] = SECRETS_FILE
# app.config["OIDC_COOKIE_SECURE"] = True
# app.config["OIDC_ID_TOKEN_COOKIE_TTL"] = 3600 # seconds
# app.config["OVERWRITE_REDIRECT_URI"] = f"{DOMAIN}/oidc/callback"
# app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
# app.config["OIDC_SCOPES"] = ["openid"]
# app.config["SECRET_KEY"] = "NotSoSecretKey1234"
# app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"

# oidc = OpenIDConnect(app)

# config = {"orgUrl": OKTA_DOMAIN, "token": okta_api}
# okta_client = OktaClient(config)

dash_app = dash.Dash(
    __name__,
    server=app,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    url_base_pathname="/",
)

dash_app.title = "Dash-Example"

server = dash_app.server
