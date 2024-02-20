

from pytest_bdd import parsers, given, when, then, scenario
from fastapi import HTTPException
from src.service.validation import Validation


## ---------- Edição de reserva com sucesso -------------

@scenario(scenario_name = "Editar reserva com sucesso", feature_name = "../feature/manage_booking.feature")
def test_edit_reservation_by_id():
    pass

@given(parsers.cfparse('Uma reserva de id "{rsv_id}", existe no bando de dados'))
def mock_reservation_service_response(rsv_id: str):

    result = Validation.get_reservation_by_id(rsv_id)
    assert result

@when(
    parsers.cfparse(
        'um usuário envia uma requisição PUT para "{url_requisition}" com as seguintes infromações data de check-in "{date_in}", data de check-out "{date_out}", cliente "{user}", acomodação "{accommodation}" e reserva {rsv_id}"' 
    ),
    target_fixture="context"
)   

def put_edite_reservation(client, context, url_requisition: str, date_in: str, date_out: str, rsv_id: str, user: str, accommodation: str):
    
    response = client.put(url_requisition, params={"id": rsv_id, "checkin_date": date_in, "checkout_date": date_out,
                                                  "accommodation_id": accommodation, "cliente_id": user})
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'o Json de resposta deve conter "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

# ---------- Editar reserva com acomodação inexistente -------------

@scenario(scenario_name = "Editar reserva com acomodação inexistente", feature_name = "../feature/manage_booking.feature")
def test_edit_reservation_data_error():
    pass

@given(parsers.cfparse('Uma reserva de id "{rsv_id}", existe no bando de dados'))
def mock_reservation_service_response_error(rsv_id: str):

    result = Validation.get_reservation_by_id(rsv_id)
    assert result

@when(
    parsers.cfparse(
        'um usuário envia uma requisição PUT para "{url_requisition}" com as seguintes infromações data de check-in "{date_in}", data de check-out "{date_out}", cliente "{user}", acomodação "{accommodation}" e reserva {rsv_id}"' 
    ),
    target_fixture="context"
)   

def put_edite_reservation_error(client, context, url_requisition: str, date_in: str, date_out: str, rsv_id: str, user: str, accommodation: str):
    
    response = client.put(url_requisition, params={"id": rsv_id, "checkin_date": date_in, "checkout_date": date_out,
                                                  "accommodation_id": accommodation, "cliente_id": user})
    context["response"] = response
    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_reservation_status_code_erro(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'o Json de resposta deve conter "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_reservation_json_erro(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context


## ----------  Editar reserva com check-out menor que check-in -------------

@scenario(scenario_name = "Editar reserva com check-out menor que check-in", feature_name = "../feature/manage_booking.feature")
def test_edit_reservation_with_error():
    pass

@given(parsers.cfparse('Uma reserva de id "{rsv_id}", existe no bando de dados'))
def mock_reservation_service_response_error(rsv_id: str):

    result = Validation.get_reservation_by_id(rsv_id)
    assert result

@when(
    parsers.cfparse(
        'um usuário envia uma requisição PUT para "{url_requisition}" com as seguintes infromações data de check-in "{date_in}", data de check-out "{date_out}", cliente "{user}", acomodação "{accommodation}" e reserva {rsv_id}"' 
    ),
    target_fixture="context"
)   

def put_edite_reservation_error(client, context, url_requisition: str, date_in: str, date_out: str, rsv_id: str, user: str, accommodation: str):
    
    response = client.put(url_requisition, params={"id": rsv_id, "checkin_date": date_in, "checkout_date": date_out,
                                                  "accommodation_id": accommodation, "cliente_id": user})
    context["response"] = response
    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 
def check_edite_reservation_status_code_erro(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'o Json de resposta deve conter "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_reservation_json_erro(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

## ----------  Deletar reserva com sucesso -------------

@scenario(scenario_name = "Deletar reserva com sucesso", feature_name = "../feature/manage_booking.feature")
def test_delete_reservation_success():
    pass

@given(parsers.cfparse('Uma reserva de id "{rsv_id}", existe no bando de dados'))
def delete_reservation_service_responser(rsv_id: str):

    result = Validation.get_reservation_by_id(rsv_id)
    assert result

@when(
    parsers.cfparse(
        'um usuário envia uma requisição DELETE para "{url_requisition}"'
        ),
    target_fixture="context"
)   

def delete_reservation(client, context, url_requisition: str):
    
    response = client.delete(url_requisition, params={})
    context["response"] = response
    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 

def delete_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(
    parsers.cfparse('o Json de resposta deve conter "{resposta_txt}"'),
    target_fixture="context"
)

def check_response_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

@then(parsers.cfparse('a reserva de id "{rsv_id}" não está mais disponível'),target_fixture="context")
def response_reservation_json_erro(context, rsv_id: str):
    
    result = Validation.get_reservation_by_id(rsv_id)
    if result is None:
        return context 

#----------Deletar reserva que não existe-----------

@scenario(scenario_name = "Deletar reserva que não existe", feature_name = "../feature/manage_booking.feature")
def test_passoInr():
    pass

@given(parsers.cfparse('Uma reserva de id "{rsv_id}", não existe no bando de dados'))
def passoDois(client, context, rsv_id: str):

    ## garantindo que não haja a reserva no banco de dados

    result = Validation.get_reservation_by_id(rsv_id)

    if result :
        response = client.delete(f"/reservation/{rsv_id}/delete", params={rsv_id})
        context["response"] = response

        assert context["response"].status_code == 200
        return context
            
    return context

@when(
    parsers.cfparse(
        'um usuário envia uma requisição DELETE para "{url_requisition}"'),target_fixture="context"
)   

def passoTres(client, context, url_requisition: str):
    
    response = client.delete(url_requisition, params={})
    context["response"] = response
    return context
    
@then(parsers.cfparse('o status do código deve ser "{status_code}"'), target_fixture="context") 

def passoQuatro(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(parsers.cfparse('o Json de resposta deve conter "{resposta_txt}"'), target_fixture="context")

def passoQuinto(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt
    return context