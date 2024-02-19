from pytest_bdd import parsers, given, when, then, scenario
import src.main as main

@scenario(scenario_name="enviar avaliação para reserva", feature_name="../feature/evaluate.feature")
def test_rating_add():
     """add rating successfully"""

@given(parsers.cfparse('o formulário foi preenchido com os dados em reservation_id = “{reservation_id}” e accommodation_id = “{accommodation_id}” e stars = “{stars}” e comment = "{comment}"'), 
        target_fixture="context")
def mock_item_service_response(context, reservation_id:str, accommodation_id:str, stars:int, comment:str):
    int_star = int(stars)
    input = [reservation_id, accommodation_id, int_star, comment]
    context = input
    return context 

@when(
    parsers.cfparse('uma requisição post foi enviada para /reservations/{reservation}/evaluate'), 
    target_fixture="context")
def send_post(context):
    context = main.rating_post(context[0], context[1], context[2], context[3])
    return context

@then(parsers.cfparse('o sistema retorna a mesagem “{mensage}”'), 
        target_fixture="context")
def check_response(context, mensage:str):
    assert context == mensage
