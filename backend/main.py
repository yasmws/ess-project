from datetime import date
from src.api import reservations 
from src.api import  users
from src.api import accommodations
from src.api import edit_accommodations
from src.api import delete_accommodations
from src.api import edite_reservation 
from src.api import delete_reservation
from src.api import historyc

from fastapi import FastAPI, HTTPException, Depends, Cookie
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse
from src.db.firebase_config import auth
import src.db.firebase_config as firebase_config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

storage = firebase_config.firebase.storage()


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

@app.post("/users/logout")
def logout_user(
        token: str
    ):
    return users.logout_user(token)


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

@app.post("/accommodation/{id}/edit")
def edit_accommodation(
        id: str,
        accommodation_name: str = None,
        accommodation_loc: str = None, 
        accommodation_bedrooms: int = None,
        accommodation_max_capacity: int = None, 
        accommodation_description: str = None,
        ):
        
        return edit_accommodations.update_accommodation(id, accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description)

@app.delete("/accommodation/{id}/delete") 
def delete_accomodation(id: str):
     return delete_accommodations.delet_accommodation(id)

@app.post("/reservation/{id}/edit")
def edit_reservation(id: str, checkin_date:str, checkout_date: str, accommodation_id: str, cliente_id: str):
     result = edite_reservation.edit_reservation(id, checkin_date, checkout_date,accommodation_id, cliente_id)
     return {"mensagem": result}

@app.delete("/reservation/{id}/delete")
def del_reservation(id: str):
    return delete_reservation.delete_reservation(id)

@app.get("/historyc/{id}")
def get_historic(id:str, checkin: str, checkout:str):
     return historyc.historyc(id, checkin, checkout)