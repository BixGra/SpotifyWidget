import os
import random
import secrets
import string

from src.tools.html_base import *

alphabet = string.ascii_letters + string.digits

songs = [
    {"image": "https://i.scdn.co/image/ab67616d0000b2735a92350866fd5e6b7a10de22", "name": "JUSTE AMIS", "artists": ["THEA"]},
    {"image": "https://i.scdn.co/image/ab67616d0000b27328933b808bfb4cbbd0385400", "name": "Knights of Cydonia", "artists": ["Muse"]},
    {"image": "https://i.scdn.co/image/ab67616d0000b273fad5111be86806be0bbbe2e2", "name": "Floral", "artists": ["Ponce", "CEYLON", "Princesse Näpalm", "Léo Lenvers"]},
    {"image": "https://i.scdn.co/image/ab67616d0000b27354a277d652eba4cd35a2e78a", "name": "Harder, Better, Faster, Stronger", "artists": ["Daft Punk"]},
    {"image": "https://i.scdn.co/image/ab67616d0000b273bd2b38759d23dba73eea6a5c", "name": "Insomnies", "artists": ["Colt"]},
    {"image": "https://i.scdn.co/image/ab67616d0000b273193c2fafdce8f116b5ca0a78", "name": "Juna", "artists": ["Clairo"]}
]

names = [
    "Test template",
    "Pink neon",
    "truc",
    "gzbifezfzef",
    "blablalbla",
    "oui c'est joli en vrai",
]


def random_string(length: int) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length))


def to_url(query_parameters: dict) -> str:
    return "?" + "&".join(map(lambda x: f"{x[0]}={x[1]}", query_parameters.items()))


def render_song(current_song: dict) -> str:
    if "name" in current_song:
        song = SONG.format(album=current_song["image"], name=current_song["name"], artists=", ".join(current_song["artists"]))
    elif "status" in current_song:
        song = SONG.format(album="", name=current_song["status"], artists="We like it quiet")
    else:
        song = SONG.format(album="", name=current_song.get("name", "Error"), artists=current_song.get("message", "Please check the website"))
    return song


def render_iframe(index: int) -> str:
    song = render_song(random.choice(songs))
    page = IFRAME.format(body=song, style=index)
    return page


def render_example(index: int) -> str:
    song = render_song(random.choice(songs))
    css = ""
    if os.path.exists(f"./src/style/style{index}.css"):
        with open(f"./src/style/style{index}.css") as f:
            lines = f.readlines()
        css = "<br>".join(map(lambda x: x.rstrip("\n").replace("  ", "&nbsp;&nbsp;"), lines))
        print(css)
    example = EXAMPLE.format(index=index, css=css)
    page = BASE.format(body=example)
    return page


def render_connect() -> str:
    page = BASE.format(body=CONNECT)
    return page


def render_main(token: str) -> str:
    main = MAIN.format(
        token=token,
        **{f"gallery_{i+1}_id": i+1 for i in range(6)},
        **{f"gallery_{i+1}_name": names[i] for i in range(6)},
    )
    page = BASE.format(body=main)
    return page
