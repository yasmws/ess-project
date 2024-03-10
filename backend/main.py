from datetime import date
import src.api.reservations as reservations
import src.api.users as users
import src.api.accommodations as accommodations

import src.api.delete_accommodations as delete_accommodations
import src.api.delete_reservation as delete_reservation
import src.api.edit_accommodations as edit_accommodations
import src.api.edite_reservation as edite_reservation
import src.api.historyc as historyc
import src.api.evaluate as evaluate
import src.api.payment_method as payment
from src.api.email_trigger import send_email

from fastapi import FastAPI, HTTPException, Depends, Cookie
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse
from src.db.firebase_config import auth
import src.db.firebase_config as firebase_config
from src.db.firebase_config import auth
import src.db.firebase_config as firebase_config
from pydantic import SecretStr
from typing import Optional

app = FastAPI()

storage = firebase_config.firebase.storage()
app.logged_user = ""

# Custom dependency to check user authentication
def get_current_user(token: str = Cookie(None)):
    if token is None:
        return RedirectResponse(url="/login")
    try:
        user = auth.get_account_info(token)
        return user
    except auth.AuthError:
        return RedirectResponse(url="/login")

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

@app.post("/accommodation/create")
def create_accommodation(
        accommodation_name: str,
        accommodation_loc: str, 
        accommodation_bedrooms: int,
        accommodation_max_capacity: int, 
        accommodation_description: str,
        accommodation_price: int,
        user_id: str
        ):
        
        return accommodations.create_accommodation(accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description, accommodation_price, user_id)

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

@app.post("/reservations/{reservation_id}/evaluate")
def rating_post(
        reservation_id:str,
        accommodation_id:str,
        stars:int,
        comment:str = ""
    ):
    return evaluate.add_rating(reservation_id, stars, comment, accommodation_id)

@app.get("/accommodation/{accommodation_id}")
def get_accommodation_by_id(
    accommodation_id: str
    ): 
    return accommodations.get_accommodation_by_id(
        accommodation_id
    )
    

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