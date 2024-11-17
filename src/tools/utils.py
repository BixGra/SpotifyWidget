import secrets
import string


alphabet = string.ascii_letters + string.digits


def random_string(length: int) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length))


def to_url(query_parameters: dict) -> str:
    return "?" + "&".join(map(lambda x: f"{x[0]}={x[1]}", query_parameters.items()))


def to_html(current_song: dict) -> str:
    if "name" in current_song:
        output = f"""<div id="frame">
        <div id="level-1">{current_song.get("name", "Name not found")}</div>
        <div id="level-2">{", ".join(current_song.get("artists", ["Artists not found"]))}</div>
        </div>"""
    elif "status" in current_song:
        output = f"""<div id="frame">
        <div id="level-1">{current_song.get("status", "Not playing")}</div>
        <div id="level-2">Sometimes, it's nice to enjoy the silence</div>
        </div>"""
    else:
        output = f"""<div id="frame">
        <div id="level-1">{current_song.get("error", "Error")}</div>
        <div id="level-2">{current_song.get("message", "Please check the website")}</div>
        </div>"""
    return output