import logging

from os import environ, urandom
from flask import Flask, request, redirect, session
from PavlokClient import PavlokClient

secret_key = environ.get("SECRET_KEY") or urandom(20)

app = Flask(__name__)
app.secret_key = secret_key

pavlok_auth = PavlokClient(
    client_id="9f421977a244d62c2209b5876bb99570889ea7cdfada094d71cbf922921ec5a2",
    client_secret="00cce70f69bd17479d8484e366190faa99be33ad536f14f8ee3b0f5a4de72c8e",
    redirect_uri="http://localhost:5000"
)

uri = pavlok_auth.authorize_url(
    response_type="code"
)

# Note that I simplified the routing level abstraction to one endpoint.
@app.route("/")
def index():
    if "access_token" in session:
        return "You are already logged in... You should be able to play the Brick Game now with Pavlok features... Access Token: " + session["access_token"]
    elif request.args.get("code"):
        token = request.args.get("code")
        session["access_token"] = token

        f = open("token", "w")
        f.write(token)
        f.close()

        return "You just logged in... You should be able to play the Brick Game now with Pavlok features... Access Token: " + session["access_token"]
    else:
        return redirect(uri)

# I intentionally made a second route to return the access token for clarity.
@app.route("/token")
def token():
    f = open("token", "r")
    token = f.read()
    if len(token) > 5:
        return token
    else:
        return "NO_TOKEN_FOUND"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
