Feature: Search for accommodations

Scenario: Procurar acomodações por localização existente
    Given existe um user com id "yasmin123" no banco de dados
    And existe uma acomodação com localização "recife" no banco de dados
    When uma requisição GET é feita para "/accommodation/list?location=recife"
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a localização "recife"

Scenario: Procurar acomodações por localização inexistente
    Given existe um user com id "yasmin123" no banco de dados
    And existe uma acomodação com localização "recife" no banco de dados
    And não existe nenhuma acomodação com localização "salvador" no banco de dados
    When uma requisição GET é feita para "/accommodation/list?location=salvador"
    Then o status da resposta a ser mostrada é "204"

Scenario: Procurar acomodações por data de check-in e check-out
    Given existe um user com id "yasmin123" no banco de dados
    And existe uma acomodação com disponibilidade de datas entre "2024-02-25" e "2023-02-29" no banco de dados
    When uma requisição GET é feita para "/accommodation/list?checkin=2024-02-25&checkout=2023-02-29"
    Then o status da resposta a ser mostrada é "200"

Scenario: Procurar acomodações por número de hóspedes
    Given existe um user com id "yasmin123" no banco de dados
    And existe uma acomodação com capacidade para "5" hóspedes no banco de dados
    When uma requisição GET é feita para "/accommodation/list?guests=5"
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve ter max_capacity maior ou igual a "5" hóspedes
