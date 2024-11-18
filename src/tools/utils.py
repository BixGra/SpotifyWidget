import os
import secrets
import string
import random

from src.tools.settings import base_url

alphabet = string.ascii_letters + string.digits

songs = [
    {"name": "JUSTE AMIS", "artists": ["THEA"]},
    {"name": "Knights of Cydonia", "artists": ["Muse"]},
    {"name": "Floral", "artists": ["Ponce", "CEYLON", "Princesse Näpalm", "Léo Lenvers"]},
    {"name": "Harder, Better, Faster, Stronger", "artists": ["Daft Punk"]}
]


def random_string(length: int) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length))


def to_url(query_parameters: dict) -> str:
    return "?" + "&".join(map(lambda x: f"{x[0]}={x[1]}", query_parameters.items()))


def to_html(current_song: dict) -> str:
    if "name" in current_song:
        output = f"""<div id="frame">
        <div id="item-1"><p id="text-1">{current_song.get("name", "Name not found")}</p></div>
        <div id="item-sep"><p id="text-sep">-</p></div>
        <div id="item-2"><p id="text-2">{", ".join(current_song.get("artists", ["Artists not found"]))}</p></div>
        </div>"""
    elif "status" in current_song:
        output = f"""<div id="frame">
        <div id="item-1"><p id="text-1">{current_song.get("status", "Not playing")}</p></div>
        <div id="item-sep"><p id="text-sep"></p></div>
        <div id="item-2"><p id="text-2">Sometimes, it's nice to enjoy the silence</p></div>
        </div>"""
    else:
        output = f"""<div id="frame">
        <div id="item-1"><p id="text-1">{current_song.get("error", "Error")}</p></div>
        <div id="item-sep"><p id="text-sep"></p></div>
        <div id="item-2"><p id="text-2">{current_song.get("message", "Please check the website")}</p></div>
        </div>"""
    return output

def to_example(index: int) -> str:
    if os.path.exists(f"./src/style/style{index}.css"):
        with open(f"./src/style/style{index}.css") as f:
            css = f.read()
        song = random.choice(songs)
        output = f"""<html>
        <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
        <head>
        <link href="{base_url}/src/style/style{index}.css" media="screen" rel="stylesheet" type="text/css"/>
        <link href="{base_url}/src/style/stylebox.css" media="screen" rel="stylesheet" type="text/css"/>
        </head>
        <body>
        <div id="frame">
            <div id="item-1"><p id="text-1">{song["name"]}</p></div>
            <div id="item-sep"><p id="text-sep"> - </p></div>
            <div id="item-2"><p id="text-2">{", ".join(song["artists"])}</p></div>
        </div>
        <div id="item-copy">
            <p id="text-copy">Triple clic and copy the box content to your OBS source "custom CSS"</p>
        </div>
        <div id="item-css">
            <p id="text-css">{css}</p>
        </div>
        </body>
        </html>"""
    else:
        output = f"""<p>Error, go back to {base_url}</p>"""
    return output