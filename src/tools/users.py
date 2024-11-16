from src.tools.spotify import spotify
from src.tools.utils import random_string
from datetime import datetime, timedelta


class Users:
    def __init__(self):
        self.data = {}

    def exists(self, user_id: str) -> bool:
        return user_id in self.data.keys()

    def create(self, token: str, refresh_token: str) -> str:
        user_id = random_string(16)
        while self.exists(user_id):
            user_id = random_string(16)
        self.data[user_id] = {
            "token": token,
            "refresh_token": refresh_token,
            "last_use": datetime.now(),
        }
        return user_id

    def get(self, user_id: str) -> str:
        self.data[user_id]["last_use"] = datetime.now()
        return self.data[user_id]["token"]

    def delete(self, user_id: str) -> None:
        del self.data[user_id]

    def refresh(self) -> None:
        limit = datetime.now() - timedelta(minutes=30)
        for user_id, user_data in self.data.items():
            if user_data["last_use"] < limit:
                self.delete(user_id)
            else:
                self.data[user_id]["token"] = spotify.refresh(user_data["refresh_token"])

users = Users()
