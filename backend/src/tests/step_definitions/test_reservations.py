
from datetime import date, datetime
from pytest_bdd import parsers, given, when, then, scenario
from src.service.validation import Validation

def format_date(date_str: str, current_format: str, desired_format: str) -> str:
    # Converte a string de data para um objeto datetime usando o formato atual
    date_obj = datetime.strptime(date_str, current_format)
    # Formata o objeto datetime de acordo com o formato desejado
    formatted_date = date_obj.strftime(desired_format)
    return formatted_date



@scenario(scenario_name = "Criar uma reserva de uma acomodação existente com sucesso", feature_name = "../feature/reservations.feature")
def test_create_reservation_by_id():
    pass

@given(parsers.cfparse('existe uma acomodação com accommodation_id "{accommodation_id}" no banco de dados'))
def mock_create_reservation_service_response(accommodation_id: str):

    result = Validation.get_accommodation_by_id(accommodation_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" com os dados da reserva nos campos: checkin: "{date_in}", checkout: "{date_out}", client_id: "{client_id}", accommodation_id: "{accommodation_id}"'
    ),
    target_fixture="context"
)   

def post_create_reservation(client, context, url_requisition: str, date_in: str, date_out: str, client_id: str, accommodation_id: str):
    
    response = client.post(url_requisition, params={"reservation_checkin": date_in,
        "reservation_checkout": date_out,
        "accommodation_id": accommodation_id,
        "client_id": client_id}
        )
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def check_create_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

# ---------- Editar reserva com acomodação inexistente -------------

@scenario(scenario_name = "Criar uma reserva de uma acomodação inexistente", feature_name = "../feature/reservations.feature")
def test_create_reservation_by_bad_acc_id():
    pass

@given(parsers.cfparse('não existe uma acomodação com id "{accommodation_id}"'))
def mock_create_reservation_service_response(accommodation_id: str):

    result = Validation.get_accommodation_by_id(accommodation_id)
    assert result is None

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" com os dados da reserva nos campos: checkin: "{date_in}", checkout: "{date_out}", client_id: "{client_id}", accommodation_id: "{accommodation_id}"'
    ),
    target_fixture="context"
)   

def post_create_reservation(client, context, url_requisition: str, date_in: str, date_out: str, client_id: str, accommodation_id: str):
    
    response = client.post(url_requisition, params={"reservation_checkin": date_in,
        "reservation_checkout": date_out,
        "accommodation_id": accommodation_id,
        "client_id": client_id}
        )
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def check_create_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context


# ---------- Criar uma reserva com cliente inexistente no banco de dados -------------

@scenario(scenario_name = "Criar uma reserva com cliente inexistente no banco de dados", feature_name = "../feature/reservations.feature")
def test_create_reservation_by_bad_client_id():
    pass

@given(parsers.cfparse('não existe um cliente cuja id é "{cli_id}"'))
def mock_create_reservation_service_response(cli_id: str):

    result = Validation.get_user_by_id(cli_id)
    assert result is None

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" com os dados da reserva nos campos: checkin: "{date_in}", checkout: "{date_out}", client_id: "{client_id}", accommodation_id: "{accommodation_id}"'
    ),
    target_fixture="context"
)   

def post_create_reservation(client, context, url_requisition: str, date_in: str, date_out: str, client_id: str, accommodation_id: str):
    
    response = client.post(url_requisition, params={"reservation_checkin": date_in,
        "reservation_checkout": date_out,
        "accommodation_id": accommodation_id,
        "client_id": client_id}
        )
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def check_create_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context


## ----------  Criar uma reserva com data de checkin depois da data de checkout -------------

@scenario(scenario_name = "Criar uma reserva com data de checkin depois da data de checkout", feature_name = "../feature/reservations.feature")
def test_create_reservation_bad_date():
    pass


@given(parsers.cfparse('existe uma acomodação com accommodation_id "{accommodation_id}" no banco de dados'))
def mock_create_reservation_service_response(accommodation_id: str):

    result = Validation.get_accommodation_by_id(accommodation_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" com os dados da reserva nos campos: checkin: "{date_in}", checkout: "{date_out}", client_id: "{client_id}", accommodation_id: "{accommodation_id}"'
    ),
    target_fixture="context"
)   

def post_create_reservation(client, context, url_requisition: str, date_in: str, date_out: str, client_id: str, accommodation_id: str):
    
    response = client.post(url_requisition, params={"reservation_checkin": date_in,
        "reservation_checkout": date_out,
        "accommodation_id": accommodation_id,
        "client_id": client_id}
        )
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def check_create_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

#----------Criar uma reserva de um cliente cuja id é a mesma daquele que criou a acomodação-----------
@scenario(scenario_name = "Criar uma reserva de um cliente cuja id é a mesma daquele que criou a acomodação", feature_name = "../feature/reservations.feature")
def test_create_reservation_equal_id():
    pass


@given(parsers.cfparse('existe uma acomodação com accommodation_id "{accommodation_id}" no banco de dados e aquele que criou a acomodação tem id "{client_id}"'))
def mock_create_reservation_service_response(accommodation_id: str):

    result = Validation.get_accommodation_by_id(accommodation_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" com os dados da reserva nos campos: checkin: "{date_in}", checkout: "{date_out}", client_id: "{client_id}", accommodation_id: "{accommodation_id}"'
    ),
    target_fixture="context"
)   

def post_create_reservation(client, context, url_requisition: str, date_in: str, date_out: str, client_id: str, accommodation_id: str):
    
    response = client.post(url_requisition, params={"reservation_checkin": date_in,
        "reservation_checkout": date_out,
        "accommodation_id": accommodation_id,
        "client_id": client_id}
        )
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def check_create_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

#----------Criar uma reserva com, pelo menos, uma das datas escolhidas indisponíveis-----------

@scenario(scenario_name = "Criar uma reserva com, pelo menos, uma das datas escolhidas indisponíveis", feature_name = "../feature/reservations.feature")
def test_create_reservation_no_vacancy():
    pass


@given(parsers.cfparse('existe uma acomodação com accommodation_id "{accommodation_id}" no banco de dados'))
def mock_create_reservation_service_response(accommodation_id: str):

    result = Validation.get_accommodation_by_id(accommodation_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" com os dados da reserva nos campos: checkin: "{date_in}", checkout: "{date_out}", client_id: "{client_id}", accommodation_id: "{accommodation_id}"'
    ),
    target_fixture="context"
)   

def post_create_reservation(client, context, url_requisition: str, date_in: str, date_out: str, client_id: str, accommodation_id: str):
    
    response = client.post(url_requisition, params={"reservation_checkin": date_in,
        "reservation_checkout": date_out,
        "accommodation_id": accommodation_id,
        "client_id": client_id}
        )
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def check_create_reservation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_reservation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context