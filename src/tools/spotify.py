import os

import requests
from requests_oauthlib import OAuth2Session

base_url = "https://www.sandbix.fr/spotifywidget"

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = f"{base_url}/callback"


authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
scope = [
    "user-read-currently-playing",
]
current_song_url = "https://api.spotify.com/v1/me/player/currently-playing"

spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
authorization_url, _ = spotify.authorization_url(authorization_base_url)
tokens = {"access_token": ""}


def get_current_song(token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(
        current_song_url,
        headers=headers
    )
    status_code = response.status_code
    current_song = {}
    match status_code:
        case 200:
            current_song_details = response.json()
            current_song["name"] = current_song_details.get("item", {}).get("name")
            current_song["artists"] = ", ".join([artist.get("name", "Error") for artist in current_song_details.get("item", {}).get("artists", "Error")])
        case 400:
            current_song["error"] = status_code
            current_song["details"] = "not connected"
        case _:
            current_song["error"] = status_code
            current_song["details"] = ""
    return current_song


def to_html(song: dict) -> str:
    html = f"""
    <div class="section">
        <div class="container">
            <div class="text">
                <span class="name">{song.get("name", "error")}</span>
                <span class="dash"> - </span>
                <span class="artists">{song.get("artists", song)}</span>
            </div>
        </div>
    </div>
    """
    return html
