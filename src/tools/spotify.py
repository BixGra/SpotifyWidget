import requests

from src.tools.settings import client_id, client_encoded, redirect_uri
from src.tools.utils import random_string, to_url

authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
current_song_url = "https://api.spotify.com/v1/me/player/currently-playing"

scope = "user-read-currently-playing"
response_type = "code"

class SpotifyClient:
    def __init__(self):
        self.state = random_string(16)

    def connect(self) -> str:
        authorization_url = authorization_base_url + to_url(
            {
                "client_id": client_id,
                "response_type": response_type,
                "state": self.state,
                "redirect_uri": redirect_uri,
                "scope": scope,
            }
        )
        return authorization_url

    def callback(self, code: str = None, state: str = None) -> (str, str):
        if self.state == state:
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
            data = response.json()
            return data["access_token"], data["refresh_token"]
        else:
            raise Exception("Error with states, please contact the service administrator.")

    @staticmethod
    def refresh(refresh_token: str) -> str:
        response = requests.post(
            token_url,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {client_encoded}",
            },
            data={
                "refresh_token": refresh_token,
                "grant_type": "refresh_token",
            }
        )
        return response.json()["access_token"]

    @staticmethod
    def get_current_song(token: str) -> dict:
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
                if current_song_details["is_playing"]:
                    current_song["name"] = current_song_details.get("item", {}).get("name", "Error")
                    current_song["artists"] = [artist.get("name", "Error") for artist in current_song_details.get("item", {}).get("artists", "Error")]
                else:
                    current_song["status"] = "Not playing"
            case _:
                current_song["error"] = status_code
                current_song["message"] = response.content
        return current_song

spotify = SpotifyClient()
