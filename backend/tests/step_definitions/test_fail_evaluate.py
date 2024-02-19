from pytest_bdd import parsers, given, when, then, scenario
import pytest
from fastapi import HTTPException
import src.main as main

@scenario(scenario_name="Nenhuma estrela foi adicionada", feature_name="../feature/evaluate.feature")
def test_rating_0_stars():
     """ it do not add rating becase not add any"""

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
def send_post_rating(client, context):
    with pytest.raises(HTTPException) as err:
        main.rating_post(context[0], context[1], context[2], context[3])
    context = err
    return context


@then(parsers.cfparse('o sistema retorna o status code "{status}" e a mesagem “{mensage}”'), 
        target_fixture="context")
def check_response_status_code(context, status:int, mensage:str):
    assert context.value.status_code == int(status)
    assert context.value.detail == mensage


@scenario(scenario_name="Mais estrelas do que o permitido", feature_name="../feature/evaluate.feature")
def test_rating_execced_stars():
     """it do not add rating becase excced star number are add"""

@scenario(scenario_name="enviar avaliação, mas a avaliação já existe para aquela reserva", feature_name="../feature/evaluate.feature")
def test_exitent_rating_():
     """it do not add rating becase excced star number are add"""