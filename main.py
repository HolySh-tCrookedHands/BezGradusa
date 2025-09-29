import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, Response

BASE_DIR = os.path.dirname(__file__)
tempPath = os.path.join(BASE_DIR, "templates")
staticPath = os.path.join(BASE_DIR, "static")

app = FastAPI()

templates = Jinja2Templates(directory=tempPath)
app.mount("/static", StaticFiles(directory=staticPath), name="static")


@app.get('/')
def go_home(request:Request):
    return RedirectResponse('/home')

@app.get("/home", response_class=HTMLResponse)
def home(request: Request, response:Response):
    user_id = request.cookies.get("user_id")
    
    if not user_id:
        return templates.TemplateResponse("index.html", context={"request": request, "notAuth":True})
    else:
        return templates.TemplateResponse("index.html", context={"request": request, "notAuth":False})

@app.get('/catalog', response_class=HTMLResponse)
def catalog(request:Request, response:Response):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return templates.TemplateResponse("catalog.html", context={"request": request, "notAuth":True})
    else:
        return templates.TemplateResponse("catalog.html", context={"request": request, "notAuth":False})

@app.get('/auth', response_class=HTMLResponse)
def reg(request:Request,response:Response, action: str = None):
    if action == 'login':
        return templates.TemplateResponse("authPage.html", context={"request": request, 'show':'login'})
    else:
        return templates.TemplateResponse("authPage.html", context={"request": request, 'show':'reg'})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
