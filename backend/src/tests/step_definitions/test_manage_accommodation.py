from pytest_bdd import parsers, given, when, then, scenario
from fastapi import HTTPException
from src.service.validation import Validation

"""
## ---------- Edição de reserva com sucesso -------------

@scenario(scenario_name = "Editar acomodação com sucesso", feature_name = "../feature/manage_accommodation.feature")
def test_edit_accommodation_by_id():
    pass

@given(parsers.cfparse('Uma acomodação de id "{rsv_id}", existe no bando de dados'))
def mock_accommodation_service_response(rsv_id: str):

    result = Validation.get_accommodation_by_id(rsv_id)
    assert result

@when(parsers.cfparse('um usuário envia uma requisição PUT para "{url_requisition}" com as seguintes infromações, descrição "{description}", max_capacity {capacity}'),
    target_fixture="context"
)   
def put_edite_accommodation(client, context, url_requisition: str, description: str, capacity: str):
    
    response = client.put(url_requisition, params={"description": description, "max_capacity": capacity})
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
def put_edite_accommodation(client, context, url_requisition: str, location: str, name: str):
    
    response = client.put(url_requisition, params={"description": location, "max_capacity": name})
    context["response"] = response
    print("RESPOSTA", response)
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


"""