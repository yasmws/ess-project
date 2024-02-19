from pytest_bdd import parsers, given, when, then, scenario
from fastapi import HTTPException
from src.service.validation import Validation
from src.schemas.reservation import ItemModel

## ---------- Edição de reserva com sucesso -------------

@scenario(scenario_name = "Histórico de user sem reservas", feature_name = "../feature/manage_historic.feature")
def test_historic_accommodation_by_id():
    pass

@given(parsers.cfparse('existe um usuário de user name "{user}" cadastrado no banco de dados '))
def mock_accommodation_service_response(user: str):

    result = Validation.get_user_by_id(user)
    assert result

@given(parsers.cfparse('o usuário {user} não tem reservas'))   
def put_edite_accommodation(user: str):
    
    response = Validation.id_has_no_reservation(user)
    assert response

@when(parsers.cfparse(' é enviado uma requisição GET para "{url_requisition}"'),
    target_fixture="context"
)   
def put_edite_accommodation_error(client, context, url_requisition: str):
    
    response = client.get(url_requisition, params={})
    context["response"] = response
    return context

@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context


