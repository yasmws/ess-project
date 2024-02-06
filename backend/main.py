import users

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Server running!!"

@app.post("/users/create")
def create_user(
        email: str,
        password:str,
        name: str = None,
        username: str = None,
        cpf: str = None
    ):
    return users.create_user(email, password)

@app.post("/users/login")
def login_user(
        email: str,
        password:str
    ):
    return users.login_user(email, password)