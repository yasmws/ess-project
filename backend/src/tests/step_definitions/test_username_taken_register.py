from pytest_bdd import parsers, given, when, then, scenario
from src.service.validation import Validation

@scenario(scenario_name = "Usuário tentou cadastrar um username já cadastrado", feature_name = "../feature/register.feature")
def test_username_taken_register():
    pass

@given(parsers.cfparse('O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "{username_check}", Email "{email_check}" , CPF "{cpf_check}" e senha "12345678"'))
def mock_username_taken_register_service_response(username_check: str, email_check: str, cpf_check: str):
    is_new_user = Validation.validade_new_user(username_check, email_check, cpf_check)
    assert is_new_user == False

@when(
    parsers.cfparse(
        'Uma requisição POST é enviada para "{url_requisition}" com Nome "{name}", Username "{username}", Email "{email}" , CPF "{cpf}" e senha "{password}"' 
    ),
    target_fixture="context"
)   

def post_username_taken_register(client, context, url_requisition: str, name: str, username: str, email: str, cpf: str, password: str):
    response = client.post(url_requisition, params={"name": name, "username": username, "email": email, "cpf": cpf, "password": password})
    context["response"] = response

    return context

@then(parsers.cfparse('O status da resposta deve ser "{status_code}"'), target_fixture="context") 

def check_username_taken_register_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(
    parsers.cfparse(
        'A resposta deve conter {resposta}'
    ),
    target_fixture="context"
)

def check_username_taken_register_response(context, resposta: str):
    
    response_data = context["response"].json()
    assert  response_data.get("detail","") in resposta

    return context