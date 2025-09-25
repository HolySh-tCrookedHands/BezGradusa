import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

BASE_DIR = os.path.dirname(__file__)
tempPath = os.path.join(BASE_DIR, "templates")
staticPath = os.path.join(BASE_DIR, "static")

app = FastAPI()

templates = Jinja2Templates(directory=tempPath)
app.mount("/static", StaticFiles(directory=staticPath), name="static")

@app.get("/home", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
