Feature: Create accommodations

    Creating the accommodations and posting them in the db

Scenario: Criar uma acomodação com um user_id existente
    Given existe uma user com user_id "yasmin123"
    And adiciona-se os dados da acomodação nos campos: "nome": "Casa da Vovó Pequena", "capacidade máxima" : "80"
    When uma requisição "POST" for enviada para "/accommodation/{id}/edit" de id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244" com os novos dados
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Accommodation updated successfully!"

"""
Scenario: Criar uma acomodação com um user_id inexistente
    Given existe uma acomodação com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    When uma requisição de "DELETE" é requisitada para "/accommodation/{id}/delete", com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    Then Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem Acomodação de id:a019fe5d-9a96-4bb1-8cfb-e7c38b612244 deletado com sucesso

Scenario: Criar uma acomodação com nome maior de 20 char
    Given existe uma acomodação com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    And os novos dados do acomodação são editados: "nome": "Casa da Vovó Pequena", "capacidade máxima" : "80"
    When uma requisição "POST" for enviada para "/accommodation/{id}/edit" de id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244" com os novos dados
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Accommodation updated successfully!"

Scenario: Criar uma acomodação com zero quartos 
    Given um id que não existe na base de dados 
    When uma requisição "DELETE" é enviada para "/accommodation/{id}/delete"
    Then o status de retorno é "404 not found"
    And a resposta da solicitação é "Accommodation not found."

"""
