# from pytest_bdd import parsers, given, when, then, scenario
# from fastapi import HTTPException
# from src.service.validation import Validation

# @scenario(scenario_name = "Procurar acomodações por localização existente", feature_name = "../feature/search.feature")
# def test_search_accommodation_by_location():
#     pass

# @given(parsers.cfparse('existe uma acomodação com localização "{location}" no banco de dados'))
# def mock_accommodation_service_response(location: str):
#     result = Validation.get_accommodation_by_location(location)
#     assert result

# @when(
#     parsers.cfparse(
#         'uma requisição GET for enviada para "{url_requisition}" e adiciona-se os dados da acomodação nos campos: location: "{location}"' 
#     ),
#     target_fixture="context"
# )
# def get_accommodation_by_location(client, context, url_requisition: str, location: str):
#     response = client.get(url_requisition, params={"location": location})
#     context["response"] = response
#     return context

# @then(parsers.cfparse('o status da resposta a ser mostrada é "{status_code}"'), target_fixture="context")
# def search_accommodation_status_code(context, status_code: str):
#     assert context["response"].status_code == int(status_code)
#     return context
# @then(
#     parsers.cfparse(
#         'a resposta deve conter a mensagem "{resposta_txt}"'
#     ),
#     target_fixture="context"
# )
# def check_response_search_accommodation_json(context, resposta_txt: str):
#     response_data = context["response"].json()
#     assert  response_data.get("detail","") in resposta_txt
#     return context

# # ---------- Procurar acomodações por localização inexistente -------------

# @scenario(scenario_name = "Procurar acomodações por localização inexistente", feature_name = "../feature/search.feature")
# def test_search_accommodation_by_bad_location():
#     pass

# @given(parsers.cfparse('não existe uma acomodação com localização "{location}" no banco de dados'))
# def mock_accommodation_service_response(location: str):
#     result = Validation.get_accommodation_by_location(location)
#     assert not result
