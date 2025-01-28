from typing import Dict
from fastapi import FastAPI, Response, HTTPException, status
from fastapi import Depends
from schema import User, UserCreate
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from datetime import timedelta
import os
from fastapi.responses import HTMLResponse

app = FastAPI()

SECRET = os.urandom(24).hex()
manager = LoginManager(SECRET, '/login', use_cookie=True, default_expiry = timedelta(minutes=20))

# fake database
fake_db = {"nome.cognome" : {"username": "nome.cognome", 'password': 'password_prova'}}


@manager.user_loader()
def load_user(user: str):
    return fake_db.get(user)

@app.post("/login")
def login(user: User, response: Response):
    name = user.username
    password = user.password
    user = load_user(name)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=name)
    )
    manager.set_cookie(response, access_token)
    return "ok"

@app.post("/reg")
def register(user: UserCreate):
    if user.password != user.password_confirm:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Errore le due password non coincidono")
    if user.username in fake_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Errore username occupato")
    
    fake_db[user.username] = {"username": user.username, "password": user.password}
    return {"message": "registrazione avvenuta con successo"}



@app.get("/info_protetta")
def profilo_utente(saluto : str , user = Depends(manager)):
	return saluto + " " + user["username"]



@app.get("/primo_ingresso")
def primo_ingr():
    return "ciao Benvenuto"


@app.get("/pagina_html", response_class=HTMLResponse)
def pagina_html():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Benvenuto</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    text-align: center;
                    padding: 20px;
                }
                h1 {
                    color: #4CAF50;
                }
                a {
                    text-decoration: none;
                    color: #4CAF50;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Benvenuto nella mia applicazione FastAPI!</h1>
            <p>Questa è una semplice pagina HTML restituita da un endpoint FastAPI.</p>
            <a href="/primo_ingresso">Vai all'endpoint /primo_ingresso</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)