from typing import Dict
from fastapi import Form,FastAPI, Response, HTTPException, status, Request
from fastapi import Depends, Query
from schema import User, UserCreate
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from datetime import timedelta
import os
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import database_py

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") 
templates = Jinja2Templates(directory="templates")
SECRET = os.urandom(24).hex()
manager = LoginManager(SECRET, '/login', use_cookie=True, default_expiry = timedelta(minutes=20))

# fake database
fake_db = {"nome.cognome" : {"username": "nome.cognome", 'password': 'password_prova'}}


@manager.user_loader()
def load_user(user: str):
    return fake_db.get(user)


@app.get("/")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "message": "","titolo": "Homepage"})


@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username in fake_db:
        credenziali = fake_db[username]
        if credenziali["username"] == username and credenziali["password"] == password:
            response = RedirectResponse(url="/home_search", status_code=303)
            access_token = manager.create_access_token(
                data=dict(sub=username)
            )
            manager.set_cookie(response, access_token)
            return response

    return templates.TemplateResponse("login.html", {"request": request, "message": "Credenziali errate!"})


@app.get("/dashboard")
def dashboard(request: Request, user = Depends(manager)):
    dati = database_py.db_get_products({})
    return templates.TemplateResponse("dashboard.html", {"request": request, "products" : dati})


@app.get("/home_search")
async def search_page(request: Request, user = Depends(manager)):
    return templates.TemplateResponse("search.html", {"request": request})


@app.get("/search")
def search(
    title: str = Query(None),
    min_quantity: int = Query(None),
    max_price: float = Query(None),
    in_stock: bool = Query(None)
):
    # Chiamata alla funzione del database per ottenere i risultati
    results = database_py.search_products(title, min_quantity, max_price, in_stock)
    return results