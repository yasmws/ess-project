

SCENARIO: Realizar com sucesso uma reserva
    Given que o usuário comum de login “ymws” se encontra na página “Realizar reserva”
    And o usuário de login “ymws” consegue visualizar a lista de reservas disponíveis e a barra de pesquisa
    When o usuário de login “ymws” escolhe a acomodação “Hotel CIn”
    And o usuário de login “ymws” salva sua escolha
    Then o usuário de login “ymws” é redirecionado para a página de “Pagamento”
    And o usuário de login “ymws” preenche a forma de pagamento
    And o usuário de login “ymws” recebe a mensagem de “reserva confirmada”
    And o usuário de login “ymws” é redirecionado para a página de “Minhas reservas”

SCENARIO: Realizar uma reserva sem estar logado
    Given que o usuário comum não logado se encontra na página “Realizar reserva”
    And o usuári comum não logado consegue visualizar a lista de reservas disponíveis e uma barra de pesquisa
    When o usuário comum não logado escolhe a acomodação “Hotel CIn”
    And o usuário comum não logado seleciona a opção “salvar”
    Then o usuário comum não logado recebe uma mensagem “Você precisa estar logado para reservar uma acomodação”
    And o usuário comum não logado é redirecionado para a página de “Login”
