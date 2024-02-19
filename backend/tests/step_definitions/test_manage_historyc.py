from pytest_bdd import parsers, given, when, then, scenario
from fastapi import HTTPException
from src.service.validation import Validation
from src.schemas.reservation import ItemModel

@scenario(scenario_name ="Histórico de user com reservas", feature_name = "../feature/manage_historic.feature")
def test_historic_accommodation_sucess():
    pass

@given(parsers.cfparse('existe um usuário de user name "{user}" cadastrado no banco de dados'))
def mock_accommodation_service_response(user: str):

    result = Validation.get_user_by_id(user)
    assert result 
    

@when(parsers.cfparse('é enviado uma requisição GET para "{url_requisition}" entre os dia "{day_in}" e "{day_out}"'),
    target_fixture="context"
)   
def put_edite_accommodation_error(client, context, url_requisition: str, day_in: str, day_out: str):
    
    response = client.get(url_requisition, params={"checkin": day_in, "checkout": day_out})
    print(response)
    context["response"] = response
    return context

@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(parsers.cfparse('o Json de resposta deve conter uma lista de reservas'),target_fixture="context")

def check_response_reservation_json_erro(context):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") 

    return context