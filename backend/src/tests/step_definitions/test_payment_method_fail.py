from pytest_bdd import parsers, given, when, then, scenario
from src.service.validation import Validation


@scenario(scenario_name="Cadastrar forma de pagamento (limite atingido)", feature_name="../feature/payment_method.feature")
def test_register_payment_method_limit_reached():
    pass

@given(parsers.cfparse('o sistema possui um registro de usuário com username "{username}" e valor de cnt igual a 3'),
       target_fixture="context")
def user_reached_methods_limit(context, username: str):
    context["valid_user"] = Validation.validate_user_payment_register(username)
    methods_cnt = Validation.get_methods_amount(username)
    context["limit_reached"] = (methods_cnt == 3)
    return context

@when(parsers.cfparse('uma requisição POST for enviada para "{req_path}" com tipo "{method_type}" e id "{method_id}"'),
      target_fixture="context")
def fail_post_payment_method(client, context, req_path: str, method_type: str, method_id: str):
    if context["limit_reached"]:
        if method_id == "None":
            context["response"] = client.post(req_path, params={"type": method_type})
            return context
        else:
            context["response"] = client.post(req_path, params={"type": method_type,"method_id": method_id})
            return context

@then(parsers.cfparse('o status da resposta deve ser "{http_status:d}"'),
      target_fixture="context")
def check_fail_response_status(context, http_status: int):
    response = context["response"]
    assert response.status_code == http_status
    return context

@then(parsers.cfparse('o JSON de resposta deve ter a mensagem "{http_detail}"'),
      target_fixture="context")
def check_fail_response_message(context, http_detail: str):
    response = context["response"].json()
    assert response["detail"] == http_detail

"""========================================================================================"""

# @scenario(scenario_name="Cadastrar forma de pagamento já cadastrada", feature_name="../feature/payment_method.feature")
# def test_conflict_register_payment_method():
#     pass

# @given(parsers.cfparse('o sistema possui um registro de usuário com username "{username}"'),
#        target_fixture="context")
# def validate_conflict_user_register(context, username: str):
#     context["valid_user"] = Validation.validate_user_payment_register(username)
#     return context

# @given(parsers.cfparse('"{username}" possui um registro de forma de pagamento com tipo "{method_type}" e id "{method_id}"'),
#        target_fixture="context")
# def validate_conflict_method_register(context, username: str, method_type: str, method_id: str):
#     if method_id == "None":
#         method_id = None

#     context["valid_method"] = Validation.validate_method_register(username, method_type, method_id)
#     return context

# @when(parsers.cfparse('uma requisição "{req_type}" for enviada para "{req_path}" com tipo "{method_type}" e id "{method_id}"'),
#       target_fixture="context")
# def post_conflict_payment_method(client, context, req_path: str, method_type: str, method_id: str):
#     if context["valid_user"] and context["valid_method"]:
#         if method_id == "None":
#             context["response"] = client.post(req_path, params={"type": method_type})
#             return context
#         else:
#             context["response"] = client.post(req_path, params={"type": method_type, "method_id": method_id})
#             return context

# @then(parsers.cfparse('o status da resposta deve ser "{http_status}"'),
#       target_fixture="context")
# def check_conflict_method_status(context, http_status: str):
#     response = context["response"]
#     assert response.status_code == int(http_status)
#     return context

# @then(parsers.cfparse('o JSON de resposta deve ter a mensagem "{http_detail}"'),
#       target_fixture="context")
# def check_conflict_method_message(context, http_detail: str):
#     response = context["response"].json()
#     assert response["detail"] == http_detail

"""========================================================================================"""

@scenario(scenario_name="Tentar atualizar dados inválidos", feature_name="../feature/payment_method.feature")
def test_invalid_update_payment_method():
    pass

@given(parsers.cfparse('o sistema possui um registro de usuário com username "{username}"'),
       target_fixture="context")
def invalid_update_validate_user_register(context, username: str):
    context["valid_user"] = Validation.validate_user_payment_register(username)
    return context

@given(parsers.cfparse('"{username}" possui uma forma de pagamento cadastrada sob o referencial "{method_refer}"'),
       target_fixture="context")
def invalid_update_validate_method_register(context, username: str, method_refer: str):
    context["valid_method"] = Validation.validate_method_refer(username, method_refer)
    if context["valid_user"] and context["valid_method"]:
        context["method_refer"] = method_refer
        return context

@when(parsers.cfparse('uma requisição PUT for enviada para "{req_path}" referente a forma de pagamento com tipo "{method_type}" e id "{method_id}"'),
      target_fixture="context")
def invalid_update_payment_method(client, context, req_path: str, method_type: str, method_id: str):
    if method_id == "None":
        context["response"] = client.put(req_path, params={"method": context["method_refer"], "type": method_type})
        return context
    else:
        context["response"] = client.put(req_path, params={"method": context["method_refer"], "type": method_type, "method_id": method_id})
        return context
    
@then(parsers.cfparse('o status da resposta deve ser "{http_status:d}"'),
      target_fixture="context")
def check_invalide_update_status(context, http_status: int):
    response = context["response"]
    assert response.status_code == http_status
    return context

@then(parsers.cfparse('o JSON de resposta deve ter a mensagem "{http_detail}"'),
      target_fixture="context")
def check_invalid_update_message(context, http_detail: str):
    response = context["response"].json()
    assert response["detail"] == http_detail
    return context
