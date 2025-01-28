from typing import List, Dict
from fastapi import FastAPI, Response, HTTPException, status
from fastapi import Depends
from schema import User, UserCreate
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from datetime import timedelta
import os

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



@app.get("/info")
def get_data(id: int):
    # Esempio di logica di gestione della richiesta
    # Puoi accedere al parametro 'id' direttamente come argomento della funzione
    # Puoi quindi utilizzare questo valore per elaborare i dati e generare una risposta

    # Esempio di generazione di una risposta
    data = {
        "id": id,
        "message": "Hai inviato una richiesta GET con il parametro 'id' corrispondente a {}".format(id)
    }
    return data


@app.get("/primo_ingresso")
def primo_ingr():
    return "ciao Benvenuto"