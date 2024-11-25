from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from src.tools.settings import base_url
from src.tools.spotify import spotify
from src.tools.users import users
from src.tools.utils import render_connect, render_main, render_iframe, render_example

scheduler = BackgroundScheduler()
scheduler.add_job(users.refresh, "interval", minutes=30, id="refresh_token")
scheduler.start()


app = FastAPI()
app.mount("/src", StaticFiles(directory="src"))


@app.get("/")
async def get_method(request: Request):
    user_id = request.cookies.get("spotify_user")
    if users.exists(user_id):
        response = HTMLResponse(render_main(user_id))
    else:
        response = HTMLResponse(render_connect())
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
            response.set_cookie(key="spotify_user", value=user_id)
        except Exception as e:
            response = JSONResponse({"error": str(e)})
    return response


@app.get("/examples/{index}")
async def get_method(index: int):
    example = render_example(index)
    response = HTMLResponse(example)
    return response


@app.get("/examples/iframe/{index}")
async def get_method(index: int):
    example = render_iframe(index)
    response = HTMLResponse(example)
    return response
