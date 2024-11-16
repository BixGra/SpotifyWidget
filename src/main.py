import os
import random
from base64 import b64encode

import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

base_url = "https://sandbix.fr/spotify-widget"

authorization_base_url = "https://accounts.spotify.com/authorize"

token_url = "https://accounts.spotify.com/api/token"

api_base_url = "https://api.meethue.com/route/api/"

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
client_encoded = b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')
scope = "user-read-currently-playing"
response_type = "code"
random_state = random.randint(1000000000, 9999999999)
redirect_uri = f"{base_url}/callback"

current_song_url = "https://api.spotify.com/v1/me/player/currently-playing"

token = None
refresh_token = None

username = None


def set_token(new_token: str):
    global token
    token = new_token


def set_refresh_token(new_refresh_token: str):
    global refresh_token
    refresh_token = new_refresh_token


def set_username(new_username: str):
    global username
    username = new_username


def to_url(query_parameters: dict) -> str:
    return "?" + "&".join(map(lambda x: f"{x[0]}={x[1]}", query_parameters.items()))


app = FastAPI()


@app.get("/")
async def get_method():
    return HTMLResponse(
        f"""<a href="{base_url}/connect">connect</a>
<a href="{base_url}/current-song">current-song</a>"""
    )


@app.get("/connect")
async def get_method():
    authorization_url = authorization_base_url + to_url(
        {
            "client_id": client_id,
            "response_type": response_type,
            "state": random_state,
            "redirect_uri": redirect_uri,
            "scope": scope,
        }
    )
    return RedirectResponse(authorization_url)


@app.get("/callback")
async def get_method(error: str = None, code: str = None, state: int = 0):
    if state == random_state:
        response = requests.post(
            token_url,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {client_encoded}",
            },
            data={
                "redirect_uri": redirect_uri,
                "grant_type": "authorization_code",
                "code": code,
            }
        )

        set_token(response.json()["access_token"])
        set_refresh_token(response.json()["refresh_token"])

        return RedirectResponse(base_url)
    else:
        return "Error with states, please contact the service administrator."


@app.get("/current-song")
async def get_method():
    current_song = {}
    response = requests.get(
        current_song_url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
    )
    status_code = response.status_code
    match status_code:
        case 200:
            current_song_details = response.json()
            current_song["name"] = current_song_details.get("item", {}).get("name", "Error")
            current_song["artists"] = [artist.get("name", "Error") for artist in current_song_details.get("item", {}).get("artists", "Error")]
        case _:
            current_song["error"] = status_code
    return current_song

