from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.responses import JSONResponse

from src.tools.settings import base_url
from src.tools.spotify import spotify
from src.tools.users import users
from src.tools.utils import to_html

scheduler = BackgroundScheduler()
scheduler.add_job(users.refresh, "interval", minutes=30, id="refresh_token")
scheduler.start()


app = FastAPI()


@app.get("/")
async def get_method(request: Request):
    user_id = request.cookies.get("user_id")
    if users.exists(user_id):
        response = HTMLResponse(
            f"""<p>Token : {user_id}</p>
            <p><a href="{base_url}/current-song/{user_id}">{base_url}/current-song/{user_id}</a> copy this link to embed the song in OBS browser source</p>
            <p><a href="{base_url}/current-song">{base_url}/current-song</a></p>
            <p><a href="{base_url}/current-song/json">{base_url}/current-song/json</a></p>
            <p><a href="{base_url}/current-song/json/{user_id}">{base_url}/current-song/json/{user_id}</a></p>"""

        )
    else:
        response = HTMLResponse(f"""<a href="{base_url}/connect">connect</a>""")
    return response


@app.get("/connect")
async def get_method():
    authorization_url = spotify.connect()
    response = RedirectResponse(authorization_url)
    return response


@app.get("/callback")
async def get_method(error: str = None, code: str = None, state: str = ""):
    if error:
        response = JSONResponse({"error": error})
    else:
        try:
            token, refresh_token = spotify.callback(code, state)
            user_id = users.create(token, refresh_token)
            response = RedirectResponse(base_url)
            response.set_cookie(key="user_id", value=user_id)
        except Exception as e:
            response = JSONResponse({"error": str(e)})
    return response


@app.get("/current-song")
async def get_method(request: Request):
    user_id = request.cookies.get("user_id")
    if users.exists(user_id):
        token = users.get(user_id)
        current_song = to_html(spotify.get_current_song(token))
        response = HTMLResponse(current_song)
    else:
        current_song = to_html({"error": "401", "message": f"Connection reset, please go to {base_url}"})
        response = HTMLResponse(current_song)
    return response


@app.get("/current-song/{user_id}")
async def get_method(user_id: str):
    if users.exists(user_id):
        token = users.get(user_id)
        current_song = to_html(spotify.get_current_song(token))
        response = HTMLResponse(current_song)
    else:
        current_song = to_html({"error": "401", "message": f"Connection reset, please go to {base_url}"})
        response = HTMLResponse(current_song)
    return response


@app.get("/current-song/json")
async def get_method(request: Request):
    user_id = request.cookies.get("user_id")
    if users.exists(user_id):
        token = users.get(user_id)
        current_song = spotify.get_current_song(token)
        response = JSONResponse(current_song)
        return response
    else:
        response = JSONResponse({"error": "401", "message": f"Connection reset, please go to {base_url}"})
    return response


@app.get("/current-song/json/{user_id}")
async def get_method(user_id: str):
    if users.exists(user_id):
        token = users.get(user_id)
        current_song = spotify.get_current_song(token)
        response = JSONResponse(current_song)
    else:
        response = JSONResponse({"error": "401", "message": f"Connection reset, please go to {base_url}"})
    return response
