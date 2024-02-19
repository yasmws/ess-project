Feature: Histórico API

Scenario: Histórico de user sem reservas

    Given existe um usuário de user name "phagp" cadastrado no banco de dados 
    And o usuário "phgp" não tem reservas
    When é enviado uma requisição GET para "/historyc/{id}"
    Then o status do código deve ser "404"
    
