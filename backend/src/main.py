import src.users as users
import src.payment_methods as payment

from fastapi import FastAPI, BackgroundTasks
from src.email_trigger import send_email
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
    username: str, 
    type: str, 
    id: str = None
    ):
    return payment.add_payment_method(username, type, id)

@app.put("/payment/update")
def update_payment_method(
    username: str,
    method: str,
    type: str = "foo",
    id: str = "foo"
    ):
    return payment.update_payment_method(username, method, type, id)

@app.delete("/payment/delete")
def delete_payment_method(
    username: str,
    method: str
    ):
    return payment.delete_payment_method(username, method)


@app.post("/email_trigger")
def send_email():
    return send_email