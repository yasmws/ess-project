

Scenario: Editar dados da acomodação
    Given existe uma acomodação com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    And os novos dados do acomodação são editados: "nome": "Casa da Vovó Pequena", "capacidade máxima" : "80"
    When uma requisição "POST" for enviada para "/accommodation/{id}/edit" de id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244" com os novos dados
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Accommodation updated successfully!"

Scenario: Deletar acomodação existente
    Given existe uma acomodação com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    When uma requisição de "DELETE" é requisitada para "/accommodation/{id}/delete", com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    Then Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem Acomodação de id:a019fe5d-9a96-4bb1-8cfb-e7c38b612244 deletado com sucesso

Scenario: Editar preço de reserva das acomodações
    Given existe uma acomodação com id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244"
    And os novos dados do acomodação são editados: "nome": "Casa da Vovó Pequena", "capacidade máxima" : "80"
    When uma requisição "POST" for enviada para "/accommodation/{id}/edit" de id "a019fe5d-9a96-4bb1-8cfb-e7c38b612244" com os novos dados
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Accommodation updated successfully!"

Scenario: Deletar acomodação inexistente
    Given um id que não existe na base de dados 
    When uma requisição "DELETE" é enviada para "/accommodation/{id}/delete"
    Then o status de retorno é "404 not found"
    And a resposta da solicitação é "Accommodation not found."