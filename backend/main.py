import users
import payment_methods as payment

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Server running!!"

@app.post("/users/create")
def create_user(
        email: str,
        password:str,
        username: str,
        name: str = None,
        cpf: str = None
    ):
    return users.create_user(
        email, password, name, username, cpf
    )

@app.post("/users/login")
def login_user(
        email: str,
        password:str
    ):
    return users.login_user(email, password)

@app.post("/payment/register_user")
def register_user(username: str):
    return payment.register_user(username)

@app.post("/payment/add")
def add_payment_method(
    username: str, type: str, key: str
    ):
    return payment.add_payment_method(username, type, key)