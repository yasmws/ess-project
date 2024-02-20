
Feature: Exibir histórico de pedidos do usuário
  As a usuário 
  I want visualizar o histórico de reservas
  so that eu posso ter acesso .

Scenario: Histórico com reserva 

    Given estou logado com o login "YVSO" e senha "@56337"
    And estou na página “MINHAS RESERVAS”
    And tenho cadastrado uma reserva 
    When  seleciono a opção de “HISTÓRICO” 
    Then é me listado uma reserva com os dados nome "Vovó pequena", 
    localização "Gravatá", descrição "Um chalé requintado", banheiros "3", 
    capacidade máxima "100" para os dias 21/02/24 a 24/02/24

Scenario: Histórico sem reserva
    Given estou logado com o login "YVSO" e senha "@56337"
    And estou na página “MINHAS RESERVAS”
    And não tenho cadastrado de nenhuma reserva 
    When  seleciono a opção de “HISTÓRICO” 
    Then é me retornado uma alerta "Nenhums reserva encontrada"

Scenario: Histórico de por data
    Given estou logado com o login "YVSO" e senha "@56337"
    And existe um cadastro de reserva com os dados nome "Vovó pequena", 
    localização "Gravatá", descrição "Um chalé requintado", banheiros "3", 
    capacidade máxima "100" para os dias 21/02/24 a 24/02/24
    When seleciono o filtro por data  "01/01/24" à "01/03/24"
    Then é visualizado a reserva na página "histórico de reserva"