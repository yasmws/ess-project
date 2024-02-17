import users
import edit_accommodations 
import delete_accommodations
import edite_reservation 
import delete_reservation
import historyc
from fastapi import FastAPI, UploadFile

# rotas da API

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
     return edite_reservation.edit_reservation(id, checkin_date, checkout_date,accommodation_id, cliente_id)

@app.delete("/reservation/{id}/delete")
def del_reservation(id: str):
    return delete_reservation.delete_reservation(id)

@app.get("/historyc/{id}")
def get_historic(id:str, checkin: str, checkout:str):
     return historyc.historyc(id, checkin, checkout)

"""@app.put("/accommodation/{id}/edit/upload_img")
def edit_img(id:str):
    return edit_image.edit_image(id)
    """