import requests
from requests_oauth2 import OAuth2BearerToken

# This is the URL to retrieve the OAuth2 token

class PavlokActions:
    PavlokTokenUrl = "http://localhost:5000/token"
    token = None

    def __init__(self):
        with requests.Session() as s:
            r = s.get(self.PavlokTokenUrl)
            self.token = r.text
            print("Pavlok Token configured as " + self.token)

    def formatted_request(self, action):
        with requests.Session() as s:
            data = {
                "reason": "Pavlok Brickbreaker Game",
                "access_token": self.token
            }

            uri = None

            if action == "vibrate":
                uri = "https://pavlok-mvp.herokuapp.com/api/v1/stimuli/vibrate"
            elif action == "beep":
                uri = "https://pavlok-mvp.herokuapp.com/api/v1/stimuli/beep/255"
            else:
                print("Action was not specified")

            if uri:
                r = s.post(uri, data=data)

                if r.status_code == requests.codes.ok:
                    print(action + " successful")
                else:
                    print(action + " didn't work, error code: " + str(r.status_code))

    def vibrate(self):
        self.formatted_request("vibrate")

    def beep(self):
        self.formatted_request("beep")
