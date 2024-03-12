from pytest_bdd import parsers, given, when, then, scenario
from src.service.validation import Validation

@scenario(scenario_name = "Login do usuário usando username", feature_name = "../feature/login.feature")
def test_username_login():
    pass

@given(parsers.cfparse('O banco de dados do sistema tem cadastrado um usuário com Nome "{name_check}", Username "{username_check}", Email "{email_check}" , CPF "{cpf_check}" e senha "12345678"'))
def mock_username_login_service_response(name_check: str, username_check: str, email_check: str, cpf_check: str):
    user = Validation.get_user_by_id(username_check)
    assert user['name'] == name_check
    assert user['username'] == username_check
    assert user['email'] == email_check
    assert user['cpf'] == cpf_check

@when(
    parsers.cfparse(
        'Uma requisição POST é enviada para "{url_requisition}" com Username "{username}" e senha "{password}"' 
    ),
    target_fixture="context"
)   

def post_username_login(client, context, url_requisition: str, username: str, password: str):
    response = client.post(url_requisition, params={"emailOrUsername": username, "password": password})
    context["response"] = response

    return context

@then(parsers.cfparse('O status da resposta deve ser "{status_code}"'), target_fixture="context") 

def check_username_login_status_code(context, status_code: str): 
    assert context["response"].status_code == int(status_code) 
    return context

@then(
    parsers.cfparse(
        'A resposta deve conter {resposta}'
    ),
    target_fixture="context"
)

def check_username_login_response(context, resposta: str):
    
    response_data = context["response"].text
    assert  response_data == resposta

    return context
