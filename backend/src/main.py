from datetime import date, datetime
import src.reservations as reservations
import src.users as users
import src.accommodations as accommodations
from typing import Dict, List

from fastapi import FastAPI, HTTPException, Depends, Cookie
from fastapi.responses import RedirectResponse
from src.firebase_config import auth

app = FastAPI()

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
        accommodation_description: str
        ):
        
        return accommodations.create_accommodation(accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description)
        
@app.post("/reservation/create")
def create_reservation(
        reservation_checkin: date,
        reservation_checkout: date,
        accommodation_id: str,
        client_id: str
        ):
        return reservations.create_reservation(client_id, accommodation_id, reservation_checkin, reservation_checkout)

@app.post("/accommodations/update_reservation_info")
def update_reservation_info(
        accommodation_id: str,
        default_price: float,
        disponibility: bool
        ):
        return accommodations.update_reservation_info(accommodation_id, default_price, disponibility)