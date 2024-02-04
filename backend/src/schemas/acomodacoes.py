from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import json

class Acomodacoes(BaseModel):
    nome: str
    id: int
    descricao: str
    num_quartos: int
    checkin: datetime
    checkout: datetime
    disponibilidade: bool  
      
class Ofertas(BaseModel):
    nome: str
    id: int
    descricao: str

class Usuarios(BaseModel):
    nome: str
    email: str
    senha: str
    ofertas: Optional[list[Acomodacoes]]
    reservas: Optional[list[Acomodacoes]]
    
class EncontrarAcomodacoes(BaseModel):
    num_quartos: int
    checkin: datetime
    checkout: datetime
    

def getDB():
    with open('./src/db/db.json','r') as dbj:
        db = json.load(dbj)
    return db

def saveDB(db):
    with open('./src/db/db.json','w') as dbj:
        json.dump(db, dbj, indent=4)
  

if __name__ == '__main__':
    teste = Acomodacoes(nome ="Casa Moranbir", id=10, descricao="lalalalalal")
    yas = Usuarios(nome="Yasmin Soares", email="yasminmwsoares@gmail.com", senha="yasmin123", ofertas=None, reservas=None)
    
    db = getDB()
    db['usuarios'].append(yas.model_dump())  # Serialize User instance to dictionary
    db['acomodacoes'].append(teste.model_dump())  # Serialize Acomodacoes instance to dictionary
    saveDB(db)
