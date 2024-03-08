Feature: Histórico API

Scenario: Histórico de user com reservas

    Given existe um usuário de user name "pedro123" cadastrado no banco de dados 
    When é enviado uma requisição GET para "/historyc/pedro123" entre os dias "2024-02-15" e "2024-02-29"                                   
    Then o status do código deve ser "200"
    And o Json de resposta deve conter uma lista de reservas

Scenario: Histórico de user sem reservas

    Given existe um usuário de user name "yasmin123" cadastrado no banco de dados 
    When é enviado uma requisição GET para "/historyc/yasmin123" entre os dias "2024-02-15" e "2024-02-29"                                   
    Then o status do código deve ser "404"
 