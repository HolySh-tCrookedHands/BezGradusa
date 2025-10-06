import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from core.DataBase import *

from core.Models import *

BASE_DIR = os.path.dirname(__file__)
tempPath = os.path.join(BASE_DIR, "templates")
staticPath = os.path.join(BASE_DIR, "static")
users = Users()
items = Items()

app = FastAPI()

templates = Jinja2Templates(directory=tempPath)
app.mount("/static", StaticFiles(directory=staticPath), name="static")


@app.get('/')
def go_home(request:Request):
    return RedirectResponse('/home')

@app.get("/home", response_class=HTMLResponse)
def home(request: Request, response:Response):
    user_id = request.cookies.get("uT")
    
    if not user_id:
        return templates.TemplateResponse("index.html", context={
            "request": request, 
            "notAuth":True,
            "sale_products":[
                {
                    'discount':50,
                    "image":'/static/image/gazirovki.jpg',
                    "name":'sahfasdh',
                    "old_price":'1000',
                    'price':"500"
                }
            ]
        }
    )
    else:
        return templates.TemplateResponse("index.html", context={"request": request, "notAuth":False})

@app.get('/catalog', response_class=HTMLResponse)
def catalog(request:Request, response:Response):
    user_id = request.cookies.get("uT")
    tonik = items.getByRank('tonik')
    beer = items.getByRank('beer')
    gazirovka = items.getByRank('gazirovka')
    juice = items.getByRank('juice')
    lemonade = items.getByRank('lemonade')
    if not user_id:
        return templates.TemplateResponse(
            "catalog.html", 
            context={
                "request": request, 
                "notAuth":True,
                "tonik":tonik,
                "beer":beer,
                "gazirovka":gazirovka,
                "juice":juice,
                "lemonade":lemonade
            }
        )
    else:
        return templates.TemplateResponse(
            "catalog.html", 
            context={
                "request": request, 
                "notAuth":False,
                "tonik":tonik,
                "beer":beer,
                "gazirovka":gazirovka,
                "juice":juice,
                "lemonade":lemonade
            }
        )

@app.get('/auth', response_class=HTMLResponse)
def reg(request:Request,response:Response, action: str = None):
    if action == 'login':
        return templates.TemplateResponse("authPage.html", context={"request": request, 'show':'login'})
    else:
        return templates.TemplateResponse("authPage.html", context={"request": request, 'show':'reg'})

@app.post('/auth/reg')
def reg(user:AuthReg, response:Response):
    login = user.login
    password = user.password
    email = user.email
    token = users.addUser(login, password, email)
    if token == 403:
        return {"msg":"user found"}
    else:
        response.set_cookie(key='uT', value=token, httponly=True)
        return {'msg':"ok"}

@app.post('/auth/login')
def login(user:AuthLogin, response:Response):
    login = user.login
    password = user.password
    token = users.loginUser(login, password)
    response.set_cookie(key='uT', value=token, httponly=True)
    return RedirectResponse('/home')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
