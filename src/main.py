from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.responses import JSONResponse

from src.tools.settings import base_url
from src.tools.spotify import spotify
from src.tools.users import users

scheduler = BackgroundScheduler()
scheduler.add_job(users.refresh, "interval", minutes=30, id="refresh_token")
scheduler.start()


app = FastAPI()


@app.get("/")
async def get_method(request: Request):
    user_id = request.cookies.get("user_id")
    if users.exists(user_id):
        response = HTMLResponse(f"""<a href="{base_url}/current-song">current-song</a>""")
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
    token = users.get(user_id)
    current_song = spotify.get_current_song(token)
    response = JSONResponse(current_song)
    return response

