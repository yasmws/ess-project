from pytest_bdd import parsers, given, when, then, scenario
from src.service.payment_service import PaymentService

@scenario(scenario_name="Cadastrar forma de pagamento (limite não atingido)", feature_name="../features/payment_method_register.feature")
def test_register_payment_method():
    pass

@given(parsers.cfparse('Given o sistema possui um registro de usuário com username "{username}" e valor de cnt menor que 3'))
def mock_payment_service_response(username: str):
    result = PaymentService.get_user(username)
    assert result

@when(parsers.cfparse('When uma requisição "{req_type}" for enviada para "{req_path}" com tipo "{method_type}" e id "{method_id}"'),
      target_fixture="context")
def post_payment_method(client, context, req_path=str, method_type=str, method_id=str|None):
    response = client.post(req_path, params={"type": method_type,"id": method_id})
    context["response"] = response
    return context

@then(parsers.cfparse('Then o status da resposta deve ser "{http_status}"'), target_fixture="context")
def check_payment_method_status(context, http_status: str):
    assert context["response"].http_status == int(http_status)
    return context

@then(parsers.cfparse('And o JSON de resposta deve ter tipo "{method_type}" e id "{method_id}"'),
      target_fixture="context")
def check_payment_method_json(context, method_type=str, method_id=str|None):
    response_data = context["response"].json()
    print(response_data)
    assert response_data.get("detail","") in method_type, method_id
    return context                                       
