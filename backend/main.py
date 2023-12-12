import users

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Server running!!"


@app.post("/users/create")
def create_user(name:str, email:str):
    return users.create_user(name, email)
