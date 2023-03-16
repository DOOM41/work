# FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Server
from uvicorn import run

# Python
import psutil
import socket

# APPS
from mixin import open_file

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get('/')
async def homepage(request: Request):
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
        }
    )


@app.get("/my_app/{app_name}", name='my_app')
async def start_app(app_name: str):
    if open_file(app_name):
        return RedirectResponse('/')
    return {'Status': 'Bad'}


@app.get("/dota-close")
async def close_dota():
    try:
        for proc in psutil.process_iter():
            p = psutil.Process(proc.pid)
            if p.name() == "dota2.exe":
                p.kill()
                break
        return RedirectResponse('/')
    except Exception as e:
        return {"Status": f"{e}"}


if __name__ == '__main__':
    run(
        app='main:app',
        host=socket.gethostbyname_ex(socket.gethostname())[-1][-1],
        reload=True
    )
