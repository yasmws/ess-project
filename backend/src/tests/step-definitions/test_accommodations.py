
from pytest_bdd import parsers, given, when, then, scenario
from fastapi import HTTPException
from src.service.validation import Validation
#from schemas.reservation import ItemModel


## ---------- Criar uma acomodação com um user_id existente -------------

"""
Scenario: Criar uma acomodação com um user_id existente
    Given existe um user com id "yasmin123" no banco de dados
    When uma requisição POST for enviada para "/accommodation/create" e adiciona-se os dados da acomodação nos campos: name: "Castelo RaTimBum", location: "Recife", bedrooms : "8", max_capacity: "16", description: "Divirta-se com as aventuras de Nino e seus amigos em um castelo mágico repleto de coisas curiosas.", user_id: "yasmin123"
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Accommodation created successfully!"
"""

@scenario(scenario_name = "Criar uma acomodação com um user_id existente", feature_name = "../feature/accommodations.feature")
def test_create_accommodation_by_id():
    pass

@given(parsers.cfparse('existe um user com id "{user_id}" no banco de dados'))
def mock_accommodation_service_response(user_id: str):

    result = Validation.get_user_by_id(user_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" e adiciona-se os dados da acomodação nos campos: name: "{name}", location: "{loc}", bedrooms : "{num_bed}", max_capacity: "{max_capacity}", description: "{description}", user_id: "{user_id}"' 
    ),
    target_fixture="context"
)   

def post_create_accommodation(client, context, url_requisition: str, name: str, loc:str, num_bed:int, max_capacity:int, description:str, user_id:str):
    
    
    response = client.post(url_requisition, params={"accommodation_name": name, "accommodation_loc":loc, 
                         "accommodation_bedrooms": num_bed, "accommodation_max_capacity": max_capacity, 
                         "accommodation_description": description, "user_id": user_id}
                        )
    
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def create_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context

# ---------- Criar acomodação com usuário inexistente -------------

@scenario(scenario_name = "Criar uma acomodação com um user_id inexistente", feature_name = "../feature/accommodations.feature")
def test_create_accommodation_by_bad_id():
    pass

@given(parsers.cfparse('não existe um user com id "{user_id}" no banco de dados'))
def mock_accommodation_service_response(user_id: str):

    result = Validation.get_user_by_id(user_id)
    assert result is None
        

@when(
    parsers.cfparse(
        'uma requisição de POST é requisitada para "{url_requisition}" e adiciona-se os dados da acomodação nos campos: name: "{name}", location: "{loc}", bedrooms : "{num_bed}", max_capacity: "{max_capacity}", description: "{description}", user_id: "{user_id}"'
    ),
    target_fixture="context"
)   

def post_create_accommodation(client, context, url_requisition: str, name: str, loc:str, num_bed:int, max_capacity:int, description:str, user_id:str):
    
    
    response = client.post(url_requisition, params={"accommodation_name": name, "accommodation_loc":loc, 
                         "accommodation_bedrooms": num_bed, "accommodation_max_capacity": max_capacity, 
                         "accommodation_description": description, "user_id": user_id}
                        )
    
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def create_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context


## ----------  Criar uma acomodação com nome cujo tamanho é maior que 20 char -------------
@scenario(scenario_name = "Criar uma acomodação com nome cujo tamanho é maior que 20 char", feature_name = "../feature/accommodations.feature")
def test_create_accommodation_by_id_with_bad_name():
    pass

@given(parsers.cfparse('existe um user com id "{user_id}" no banco de dados'))
def mock_accommodation_service_response(user_id: str):

    result = Validation.get_user_by_id(user_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST for enviada para "{url_requisition}" e adiciona-se os dados da acomodação nos campos: name: "{name}", location: "{loc}", bedrooms : "{num_bed}", max_capacity: "{max_capacity}", description: "{description}", user_id: "{user_id}"' 
    ),
    target_fixture="context"
)   

def post_create_accommodation(client, context, url_requisition: str, name: str, loc:str, num_bed:int, max_capacity:int, description:str, user_id:str):
    
    
    response = client.post(url_requisition, params={"accommodation_name": name, "accommodation_loc":loc, 
                         "accommodation_bedrooms": num_bed, "accommodation_max_capacity": max_capacity, 
                         "accommodation_description": description, "user_id": user_id}
                        )
    
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def create_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context


## ----------  Criar uma acomodação com zero quartos -------------

@scenario(scenario_name = "Criar uma acomodação com zero quartos", feature_name = "../feature/accommodations.feature")
def test_create_accommodation_by_id_bad_num_bed():
    pass

@given(parsers.cfparse('existe um user com id "{user_id}" no banco de dados'))
def mock_accommodation_service_response(user_id: str):

    result = Validation.get_user_by_id(user_id)
    assert result

@when(
    parsers.cfparse(
        'uma requisição POST é enviada para "{url_requisition}" e adiciona-se os dados da acomodação nos campos: name: "{name}", location: "{loc}", bedrooms : "{num_bed}", max_capacity: "{max_capacity}", description: "{description}", user_id: "{user_id}"' 
    ),
    target_fixture="context"
)   

def post_create_accommodation(client, context, url_requisition: str, name: str, loc:str, num_bed:int, max_capacity:int, description:str, user_id:str):
    
    
    response = client.post(url_requisition, params={"accommodation_name": name, "accommodation_loc":loc, 
                         "accommodation_bedrooms": num_bed, "accommodation_max_capacity": max_capacity, 
                         "accommodation_description": description, "user_id": user_id}
                        )
    
    context["response"] = response

    return context
    
@then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context") 
def create_accommodation_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context
@then(
    parsers.cfparse(
        'a resposta deve conter a mensagem "{resposta_txt}"'
    ),
    target_fixture="context"
)

def check_response_create_accommodation_json(context, resposta_txt: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta_txt

    return context