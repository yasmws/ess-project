from pytest_bdd import parsers, given, when, then, scenario
from fastapi import HTTPException
from src.service.validation import Validation
from src.schemas.reservation import ItemModel


## ---------- Edição de reserva com sucesso -------------

@scenario(scenario_name = "Editar acomodação com sucesso", feature_name = "../feature/manage_accommodation.feature")
def test_edit_accommodation_by_id():
    pass

@given(parsers.cfparse('Uma acomodação de id "{rsv_id}", existe no bando de dados'))
def mock_accommodation_service_response(rsv_id: str):

    result = Validation.get_accommodation_by_id(rsv_id)
    assert result

@when(parsers.cfparse('um usuário envia uma requisição PUT para "{url_requisition}" com as seguintes infromações, descrição "{desc}", max_capacity "{num}"'),
    target_fixture="context"
)   
def put_edite_accommodation(client, context, url_requisition: str, desc: str, num: int):
    
    response = client.put(url_requisition, params={"description": desc, "max_capacity": int(num)})
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(parsers.cfparse('o Json de resposta deve conter "{resposta_txt}"'),target_fixture="context")
def check_response_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    print(response_data)
    assert  response_data.get("detail","") in resposta_txt

    return context


## ---------- Editar acomodação com campos inválidos -------------

@scenario(scenario_name = "Editar acomodação com campos inválidos", feature_name = "../feature/manage_accommodation.feature")
def test_edit_accommodation_error():
    pass

@given(parsers.cfparse('Uma acomodação de id "{rsv_id}", existe no bando de dados'))
def accommodation_service_response_error(rsv_id: str):

    result = Validation.get_accommodation_by_id(rsv_id)
    assert result

@when(parsers.cfparse('um usuário envia uma requisição PUT para "{url_requisition}" com as seguintes infromações, location "{location}", name "{name}"'),
    target_fixture="context"
)   
def put_edite_accommodation_error(client, context, url_requisition: str, location: str, name: str):
    
    response = client.put(url_requisition, params={"location": location , "name": name})
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(parsers.cfparse('o Json de resposta deve conter "{resposta_txt}"'),target_fixture="context")
def check_response_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

#------------------------Excluir acomodação sem reserva---------------------------

@scenario(scenario_name = "Excluir acomodação sem reserva", feature_name = "../feature/manage_accommodation.feature")
def test_delete_accommodation_error():
    pass

@given(parsers.cfparse('Uma acomodação de id "{rsv_id}", existe no bando de dados'))
def accommodation_service_response_error(rsv_id: str):

    result = Validation.get_accommodation_by_id(rsv_id)
    assert result

@when(parsers.cfparse('um usuário envia uma requisição DELETE para "{url_requisition}"'),
    target_fixture="context"
)   
def put_edite_accommodation_error(client, context, url_requisition: str):
    
    response = client.delete(url_requisition, params={})
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(parsers.cfparse('o Json de resposta deve conter "{resposta_txt}"'),target_fixture="context")
def check_response_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context