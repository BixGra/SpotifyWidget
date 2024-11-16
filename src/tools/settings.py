import os
from base64 import b64encode


base_url = os.getenv("SPOTIFY_BASE_URL")
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
client_encoded = b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')
redirect_uri = f"{base_url}/callback"
