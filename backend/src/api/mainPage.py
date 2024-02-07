from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from src.schemas.acomodacoes import Acomodacoes, Ofertas, Usuarios, EncontrarAcomodacoes, getDB, saveDB

router = APIRouter()
""" 
@router.post("/cadastrar_usuario/", status_code=201, tags=['usuarios'], response_model=Usuarios)
async def cadastrar_usuario(nome: str, email: str, senha: str):
    db = getDB()
    
    # Verificar se o usuário já existe
    for usuario in db['usuarios']:
        if usuario['email'] == email:
            raise HTTPException(status_code=422, detail='Já existe esse usuário na plataforma')

    # Validar o nome
    if not nome:
        raise HTTPException(status_code=422, detail='Nome inválido!')
    
    # Validar o email
    if not email or "@" not in email:
        raise HTTPException(status_code=422, detail='E-mail inválido!')

    # Validar a senha
    if len(senha) < 6 or not senha:
        raise HTTPException(status_code=422, detail='Senha inválida!')

    # Criar o novo usuário com os dados fornecidos
    novo_usuario = {"nome": nome, "email": email, "senha": senha}

    # Adicionar o novo usuário ao banco de dados
    db['usuarios'].append(novo_usuario.dict())
    saveDB(db)

    return novo_usuario
"""

@router.post("/validar_busca_acomodacoes/", tags=['acomodacoes'])
async def validar_busca_acomodacoes(parametros_busca: EncontrarAcomodacoes):
    checkin_with_timezone = parametros_busca.checkin.replace(tzinfo=timezone.utc)
    errors = []
    # Validar cidade
    if not parametros_busca.cidade:
        errors.append("O campo cidade é obrigatório.")
    # Validar num_quartos
    if parametros_busca.num_quartos <= 0:
        errors.append("O número de quartos deve ser maior que zero.")
    # Validar checkin e checkout
    if not parametros_busca.checkin or not parametros_busca.checkout:
        errors.append("As datas de check-in e check-out são obrigatórias.")
    elif parametros_busca.checkin >= parametros_busca.checkout:
        errors.append("A data de check-in deve ser anterior à data de check-out.")
    elif checkin_with_timezone < datetime.now(timezone.utc):
        errors.append("A data de check-in deve ser no futuro.")

    # Se houver erros, levantar uma exceção HTTP com detalhes dos erros
    if errors:
        raise HTTPException(status_code=422, detail=errors)

    # Se não houver erros, redirecionar para a rota 'mostrar_acomodacoes' com os parâmetros de busca
    return RedirectResponse(url="/mostrar_acomodacoes/?cidade={}&num_quartos={}&checkin={}&checkout={}".format(
        parametros_busca.cidade, parametros_busca.num_quartos, parametros_busca.checkin, parametros_busca.checkout
    ))
    
@router.post("/cadastrar_usuario/", status_code=201, tags=['usuarios'], response_model=Usuarios)
async def cadastrar_usuario(usuario: Usuarios):
    db = getDB()
    
    # Verificar se o usuário já existe
    for user in db['usuarios']:
        if user['email'] == usuario.email:
            raise HTTPException(status_code=422, detail='Já existe um usuário registrado com este e-mail')

    # Converter o objeto de usuário em um dicionário
    novo_usuario = usuario()

    # Adicionar o novo usuário ao banco de dados
    db['usuarios'].append(novo_usuario)

    # Salvar as alterações no banco de dados
    saveDB(db)

    return novo_usuario
    
@router.get("/mostrar_acomodacoes/", status_code=200, tags=['acomodacoes'], response_model=list[Acomodacoes])
async def mostrar_acomodacoes(parametros_busca: EncontrarAcomodacoes):
    db = getDB()
    acomodacoes_filtradas = []

    for acomodacao in db['acomodacoes']:
        # Verificar se os parâmetros de busca correspondem exatamente aos parâmetros da acomodação
        if (
            acomodacao['cidade'] == parametros_busca.cidade and
            acomodacao['num_quartos'] == parametros_busca.num_quartos and
            acomodacao['checkin'] == parametros_busca.checkin and
            acomodacao['checkout'] == parametros_busca.checkout
        ):
            acomodacoes_filtradas.append(acomodacao)

    # Se não houver acomodações, levantar um erro
    if not acomodacoes_filtradas:
        raise HTTPException(status_code=404, detail="Não temos acomodações para a busca selecionada!")

    return acomodacoes_filtradas
        

