import os

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


def get_current_song() -> dict:
    current_song = {}
    current_song_details = spotify.get(current_song_url).json()
    print(current_song_details)
    print(type(current_song_details))
    current_song["name"] = current_song_details.get("item", {}).get("name")
    current_song["artists"] = ", ".join([artist.get("name", "Error") for artist in current_song_details.get("item", {}).get("artists", "Error")])
    return current_song


def to_raw(song: dict) -> str:
    raw = f"""{song.get("name", "error")} - {song.get("artists", song)}"""
    return raw


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
