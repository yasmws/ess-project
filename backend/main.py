from datetime import date
from src.api import reservations
from src.api import users
from src.api import accommodations

from src.api import delete_accommodations
from src.api import delete_reservation
from src.api import edit_accommodations
from src.api import edite_reservation
from src.api import historyc
from src.api import evaluate
from src.api import payment_method as payment
from src.api.email_trigger import send_email

from fastapi import FastAPI, HTTPException, Depends, Cookie
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.db.firebase_config import auth
from src.db import firebase_config
from pydantic import SecretStr
from typing import Optional


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


storage = firebase_config.firebase.storage()
app.logged_user = ""

def get_logged_user():
     return users.get_username_from_email(app.logged_user)

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
        password:str
    ):
    if app.logged_user:
        raise HTTPException(status_code=400, detail="Falha ao realizar login: Usuário já está logado")
    
    if users.is_email(emailOrUsername):
        msg = users.login_user(emailOrUsername, password)
        app.logged_user = emailOrUsername
        return msg
    
    #Se não for um email, é um username
    #Para logar o email é consultado a partir desse username
    email = users.get_email_from_username(emailOrUsername)
    msg = users.login_user(email, password)
    app.logged_user = email
    return msg

@app.post("/users/logout")
def logout_user():
    if app.logged_user:
        app.logged_user = ""
        return "Usuário deslogado com sucesso!"
    raise HTTPException(status_code=400, detail="Falha ao realizar logout: Usuário não estava logado.")

@app.post("/accommodation/create")
def create_accommodation(
        accommodation_name: str,
        accommodation_loc: str, 
        accommodation_bedrooms: int,
        accommodation_max_capacity: int, 
        accommodation_description: str,
        user_id: str
        ):
        
        return accommodations.create_accommodation(accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description, user_id)

@app.post("/accommodation/create/upload_img")
async def upload(accommodation_id: str, file: UploadFile = File(...)):
    try:
        
        with open(file.filename, "wb") as buffer:
            buffer.write(await file.read())

        # Upload the file to Firebase Storage
        storage.child("accommodation").child(accommodation_id).put(file.filename)
        
        return "Imagem adicionada com sucesso"
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

@app.post("/reservation/create")
def create_reservation(
        reservation_checkin: date,
        reservation_checkout: date,
        accommodation_id: str,
        client_id: str
        ):
        return reservations.create_reservation(client_id, accommodation_id, reservation_checkin, reservation_checkout)

@app.post("/reservations/evaluate/{reservation_id}")
def rating_post(
        reservation_id:str,
        accommodation_id:str,
        stars:int,
        comment:str = ""
    ):
    return evaluate.add_rating(reservation_id, stars, comment, accommodation_id)

@app.get("/reservations/{reservation_id}/rating")
def rating_post(
        reservation_id:str,
        accommodation_id:str,
    ):
    return evaluate.get_rating(reservation_id, accommodation_id)


@app.get("/accommodation/list")
def get_accommodations(
        location: str = None,
        checkin: date = None,
        checkout: date = None,
        guests: int = None
    ):
    return accommodations.get_accommodations(
        location,
        checkin,
        checkout,
        guests
    )

@app.put("/accommodation/{id}/edit")
def edit_accommodation(
        id: str,
        name: Optional[str] = None,
        location: Optional[str] = None,
        bedrooms: Optional[int] = None,
        max_capacity: Optional[int] = None, 
        description: Optional[str] = None,
        ):
        
        return edit_accommodations.update_accommodation(id, name, location, 
                         bedrooms, max_capacity, 
                         description)

@app.delete("/accommodation/{id}/delete") 
def delete_accomodation(id: str):
     return delete_accommodations.delet_accommodation(id)

@app.put("/reservation/{id}/edit")
def edit_reservation(id: str, checkin_date:str, checkout_date: str, accommodation_id: str, cliente_id: str):
     return edite_reservation.edit_reservation(id, checkin_date, 
                                               checkout_date,accommodation_id, cliente_id)
     
@app.delete("/reservation/{id}/delete")
def del_reservation(id: str):
    return delete_reservation.delete_reservation(id)

@app.get("/historyc/{id}")
def get_historic(id:str, checkin: str, checkout:str):
     return historyc.historyc(id, checkin, checkout)

@app.post("/payment/{id}/add")
def add_payment_method(
    id: str, 
    type: str, 
    method_id: str = None
    ):
    return payment.add_payment_method(id, type, method_id)

@app.put("/payment/{id}/update")
def update_payment_method(
    id: str,
    method: str,
    type: str,
    method_id: str = None
    ):
    return payment.update_payment_method(id, method, type, method_id)

@app.delete("/payment/{id}/delete")
def delete_payment_method(
    id: str,
    method: str
    ):
    return payment.delete_payment_method(id, method)

@app.post("/email_trigger")
def send_email():
    return send_email
