from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from oauthlib.oauth2 import InvalidGrantError
from requests.auth import HTTPBasicAuth

from src.tools.spotify import *

app = FastAPI()


@app.get("/")
async def get_method():
    current_song = get_current_song(tokens["access_token"])
    return current_song


@app.get("/json")
async def get_method():
    current_song = get_current_song(tokens["access_token"])
    return current_song


@app.get("/connect")
async def get_method():
    return RedirectResponse(authorization_url)


@app.get("/callback")
async def get_method(code, state):
    authorization_response = f"{redirect_uri}/?code={code}&state={state}"
    auth = HTTPBasicAuth(client_id, client_secret)
    for _ in range(3):
        try:
            token_json = spotify.fetch_token(token_url=token_url, auth=auth, authorization_response=authorization_response)
            tokens["access_token"] = token_json.get("access_token")
            return RedirectResponse(base_url)
        except InvalidGrantError:
            pass
    return {"error": "invalid grant error"}
