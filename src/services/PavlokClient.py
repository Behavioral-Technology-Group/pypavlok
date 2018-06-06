from requests_oauth2 import OAuth2

class PavlokClient(OAuth2):
    site = "https://pavlok-mvp.herokuapp.com"
    authorization_url = "/oauth/authorize"
    token_url = "/oauth/token"
    scope_sep = " "
    client_id = None
    client_secret = None
    redirect_uri = None
