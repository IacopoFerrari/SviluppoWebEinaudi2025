from pydantic import BaseModel
from fastapi import FastAPI, Depends, Request, Security, Response
from fastapi_login import LoginManager

app = FastAPI()
SECRET_KEY = "jndajnagd87g8abag8bab"


manager = LoginManager(
    SECRET_KEY,
    algorithm="HS256",
    token_url="/login",
    use_cookie=True,
    use_header=False,
    cookie_name='access-token'
)

cred = {"user": {"username": "user", "password": "password", "secret_code": 13467328},
        "user2": {"username": "user2", "password": "234irhwefkdjnwerf0", "secret_code": 876763782},
        "admin": {"username": "admin", "password": "admin"}}


class LoginClass(BaseModel):
    username: str
    password: str


class PasswordChangeClass(BaseModel):
    username: str
    new_password: str

class CheckClass(BaseModel):
    code: int

@manager.user_loader()
def load_user(username: str):
    return cred[username]


@app.post("/login")
def login(data: LoginClass, response: Response):
    if data.username in cred.keys():
        username = data.username
        if cred[username]["password"] == data.password:
            token = manager.create_access_token(
                data={'sub': data.username},
            )
            manager.set_cookie(response, token)
            return {"status": 200, "access-token": token}
    return {"message": "credenziali non valide"}


@app.post("/change_password")
def change_password(data: PasswordChangeClass, user = Depends(manager)):
    if user["username"] != "admin":
        return {"message": "devi essere l'utente admin con password admin per cambiare le password"}
    if data.username in cred.keys():
        cred[data.username]["password"] = data.new_password
        return{"message": f"Password cambiata per l'utente {data.username}"}

@app.get("/secret_code")
def secret_code(user=Depends(manager)):
    print(user)
    if user["username"] == "admin":
        return {"message": "qui non c'è niente per te"}
    return{"secret_code": user["secret_code"]}

@app.post("/check")
def check(data: CheckClass):
    if data.code == 13467328 + 876763782:
        return {"message": "codice corretto!"}
    return{"message": "codice sbagliato!"}


