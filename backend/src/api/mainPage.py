from fastapi import APIRouter, Depends, HTTPException
from src.schemas.acomodacoes import Acomodacoes, Ofertas, Usuarios, EncontrarAcomodacoes, getDB, saveDB

router = APIRouter()

@router.post("/cadastrar_usuario/", status_code=201, tags=['usuarios'], response_model=Usuarios)
async def cadastrar_usuario(usuario:Usuarios):
    db = getDB()
    if usuario.model_dump() in db['usuarios']:
        raise HTTPException(status_code=422, detail='Já existe esse usuario na plataforma')
    if len(usuario.senha) < 6:
        raise HTTPException(status_code=422, detail='Senha inválida!')
    db['usuarios'].append(usuario.model_dump())
    saveDB(db)
    return usuario

@router.get("/mostrar_acomodacoes/", status_code=201, tags=['acomodacoes'], response_model=list[Acomodacoes])
async def mostrar_acomodacoes(parametros_busca: EncontrarAcomodacoes):
    params = parametros_busca.model_dump()
    valids_params = [par for par in params.keys() if params[par] is not None]
    
        

