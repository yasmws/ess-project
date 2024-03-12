from pytest_bdd import parsers, given, when, then, scenario
from src.service.validation import Validation


@scenario(scenario_name="Cadastrar forma de pagamento (limite não atingido)", feature_name="../feature/payment_method.feature")
def test_register_payment_method():
    pass

@given(parsers.parse('o sistema possui um registro de usuário com username "{username}" e valor de cnt menor que 3'),
       target_fixture="context")
def validate_payment_service_user(context, username: str):
    register = Validation.validate_user_payment_register(username)
    methods_cnt = Validation.get_methods_amount(username)
    under_limit = (methods_cnt < 3)

    context["valid_user"] = register
    context["limit_reached"] = not under_limit
    return context

@when(parsers.cfparse('uma requisição POST for enviada para "{req_path}" com tipo "{method_type}" e id "{method_id}"'),
      target_fixture="context")
def post_payment_method(client, context, req_path: str, method_type: str, method_id: str):
    if context["valid_user"] and not context["limit_reached"]:
        if method_id == "None":
            context["response"] = client.post(req_path, params={"type": method_type})
            return context
        else:
            context["response"] = client.post(req_path, params={"type": method_type, "method_id": method_id})
            return context

@then(parsers.cfparse('o status da resposta deve ser "{http_status:d}"'),
      target_fixture="context")
def check_reponse_status(context, http_status: int):
    response = context["response"]
    assert response.status_code == http_status
    return context

@then(parsers.cfparse('o JSON de resposta deve ter a mensagem "{http_detail}"'),
      target_fixture="context")
def check_response_message(context, http_detail: str):
    response = context["response"].json()
    assert response["detail"] == http_detail

"""========================================================================================"""

@scenario(scenario_name="Atualizar forma de pagamento", feature_name="../feature/payment_method.feature")
def test_update_payment_method():
    pass

@given(parsers.cfparse('o sistema possui um registro de usuário com username "{username}"'),
       target_fixture="context")
def update_validate_user_register(context, username: str):
    context["valid_user"] = Validation.validate_user_payment_register(username)
    return context

@given(parsers.cfparse('"{username}" possui uma forma de pagamento cadastrada sob o referencial "{method_refer}"'),
       target_fixture="context")
def update_validate_method_register(context, username: str, method_refer: str):
    context["valid_method"] = Validation.validate_method_refer(username, method_refer)
    if context["valid_user"] and context["valid_method"]:
        context["method_refer"] = method_refer
        return context

@when(parsers.cfparse('uma requisição PUT for enviada para "{req_path}" referente a forma de pagamento com tipo "{method_type}" e id "{method_id}"'),
      target_fixture="context")
def update_payment_method(client, context, req_path: str, method_type: str, method_id: str):
    if method_type == "foo" and method_id == "foo":
        context["response"] = client.put(req_path, params={"method": context["method_refer"]})
        return context
    elif method_type == "foo" and method_id == "None":
        context["response"] = client.put(req_path, params={"method": context["method_refer"], "method_id": None})
        return context
    elif method_type != "foo" and method_id == "foo":
        context["response"] = client.put(req_path, params={"method": context["method_refer"], "type": method_type})
        return context
    elif method_type != "foo" and method_id == "None":
        context["response"] = client.put(req_path, params={"method": context["method_refer"], "type": method_type, "method_id": None})
        return context
    else:
        context["response"] = client.put(req_path, params={"method": context["method_refer"], "type": method_type, "method_id": method_id})
        return context
    
@then(parsers.cfparse('o status da resposta deve ser "{http_status:d}"'),
      target_fixture="context")
def check_update_status(context, http_status: int):
    response = context["response"]
    assert response.status_code == http_status
    return context

@then(parsers.cfparse('o JSON de resposta deve ter a mensagem "{http_detail}"'),
      target_fixture="context")
def check_update_message(context, http_detail: str):
    response = context["response"].json()
    assert response["detail"] == http_detail
    return context

"""========================================================================================"""

@scenario(scenario_name="Deletar forma de pagamento (operação sucedida)", feature_name="../feature/payment_method.feature")
def test_delete_payment_method():
    pass

@given(parsers.cfparse('o sistema possui um registro de usuário com username "{username}"'),
       target_fixture="context")
def delete_validate_user_register(context, username: str):
    context["valid_user"] = Validation.validate_user_payment_register(username)
    return context

@given(parsers.cfparse('"{username}" possui uma forma de pagamento cadastrada sob o referencial "{method_refer}"'),
       target_fixture="context")
def delete_validate_method_register(context, username: str, method_refer: str):
    context["valid_method"] = Validation.validate_method_refer(username, method_refer)
    if context["valid_user"] and context["valid_method"]:
        context["method_refer"] = method_refer
        return context

@when(parsers.cfparse('uma requisição DELETE for enviada para "{req_path}" referente a essa forma de pagamento'),
      target_fixture="context")
def delete_payment_method(client, context, req_path: str):
    context["response"] = client.delete(req_path, params={"method": context["method_refer"]})
    return context

@then(parsers.cfparse('o status da resposta deve ser "{http_status:d}"'),
      target_fixture="context")
def check_delete_status(context, http_status: int):
    response = context["response"]
    assert response.status_code == http_status
    return context

@then(parsers.cfparse('o JSON de resposta deve ter a mensagem "{http_detail}"'),
      target_fixture="context")
def check_delete_message(context, http_detail: str):
    response = context["response"].json()
    assert response["detail"] == http_detail
