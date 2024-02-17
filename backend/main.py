import users

from fastapi import FastAPI, HTTPException
from pydantic import SecretStr

app = FastAPI()

app.logged_user = ""

@app.get("/")
def read_root():
    return "Server running!!"

@app.post("/users/create")
def create_user(
        name: str,
        username:str,
        email: str,
        cpf: str,
        password: str
    ):
    users.check_register_fields(name.strip(), username, email, cpf, password)
    users.check_existing_fields(username, email, cpf)

    return users.create_user(name, username, email, cpf, password)

@app.post("/users/login")
def login_user(
        emailOrUsername: str,
        password:SecretStr 
    ):
    if app.logged_user:
        return "Usuário já está logado"
    
    if users.is_email(emailOrUsername):
        msg = users.login_user(emailOrUsername, password.get_secret_value())
        app.logged_user = emailOrUsername
        return msg
    
    #Se não for um email, é um username
    #Para logar o email é consultado a partir desse username
    email = users.get_email_from_username(emailOrUsername)
    msg = users.login_user(email, password.get_secret_value())
    app.logged_user = email
    return msg

@app.post("/users/logout")
def logout_user():
    if app.logged_user:
        app.logged_user = ""
        return "Usuário deslogado com sucesso!"
    raise HTTPException(status_code=400, detail="Falha ao realizar logout: Usuário não estava logado.")