import users
import edit_accommodations as accommodations_edit
import delete_accommodations as accommodation_delete
import history_reservation as history
from fastapi import FastAPI

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

@app.post("/accommodation/edit")
def create_accommodation(
        accommodation_id: str,
        accommodation_name: str = None,
        accommodation_loc: str = None, 
        accommodation_bedrooms: int = None,
        accommodation_max_capacity: int = None, 
        accommodation_description: str = None
        ):
        
        return accommodations_edit.update_accommodation(accommodation_id, accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description)

@app.get("/accommodation/delete") #o post é obrigatório que o usuário coloque parametro? ou pode ser um parametro interno que estamos trabalhando. Por exemplo, id o user logado e registrado no back
def delete_accomodation(id: str):
     return  accommodation_delete.delet_accommodation(id)

""" @app.post("/historyc")
def get_hystoric_by_id(start_date:str,end_date:str ):
     return history.get_history(start_date, end_date)"""