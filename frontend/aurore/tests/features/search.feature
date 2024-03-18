Feature: Busca de Acomodações

Scenario: Buscar acomodações sem nenhum parâmetro
    Given Estou na tela "Busca de acomodações"
    When Clico no botão de busca
    Then Vejo os resultados da busca com acomodações disponíveis

Scenario: Buscar acomodações disponíveis por localização
    Given Estou na tela "Busca de acomodações"
    When Preencho o formulário de busca com Localização "nice"
    And Clico no botão de busca
    Then Vejo os resultados da busca com acomodações disponíveis

Scenario: Buscar acomodações com data de check-in maior que check-out
    Given Estou na tela "Busca de acomodações"
    When Preencho o formulário de busca com Localização "Recife", Check-in "2024-03-15", Check-out "2024-03-12" e Número de Hóspedes "2"
    And Clico no botão de busca
    Then Vejo uma mensagem de erro indicando que a data de check-in é maior que a data de check-out
