#!/usr/bin/env python3
# Install dependencies with:
# pip install flask requests requests_oauth2
import os
import logging
import requests

from requests_oauth2 import OAuth2BearerToken
from flask import Flask, request, redirect, session
from requests_oauth2 import OAuth2


class PavlokClient(OAuth2):
    site = "https://pavlok-mvp.herokuapp.com"
    authorization_url = "/oauth/authorize"
    token_url = "/oauth/token"
    scope_sep = " "


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(20)


pavlok_auth = PavlokClient(
    client_id="9f421977a244d62c2209b5876bb99570889ea7cdfada094d71cbf922921ec5a2",
    client_secret="00cce70f69bd17479d8484e366190faa99be33ad536f14f8ee3b0f5a4de72c8e",
    redirect_uri="http://localhost:5000",
)


@app.route("/")
def index():
	session["code"] = request.args.get("code")
	print(session)
	return redirect("/pavlok/")


@app.route("/pavlok/")
def pavlok_index():
    if not session.get("access_token"):
        return redirect("/pavlok/oauth2callback")
    with requests.Session() as s:
        s.auth = OAuth2BearerToken(session["access_token"])
        data = {"reason" :"Python", "access_token": session["access_token"]}
        r = s.post("https://pavlok-mvp.herokuapp.com/api/v1/stimuli/beep/" + "255", data=data)
    r.raise_for_status()
    return "The beep happened :)"



@app.route("/pavlok/oauth2callback")
def pavlok_oauth2callback():	
    code = session["code"]
    error = request.args.get("error")
    print (request)

    if error:
        return "error :( {!r}".format(error)
    if not code:
        return redirect(pavlok_auth.authorize_url(
            #scope=["profile", "email"],
            response_type="code",
        ))
    data = pavlok_auth.get_token(
        code=code,
        grant_type="authorization_code",
    )
    session["access_token"] = data.get("access_token")
    return redirect("/")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)