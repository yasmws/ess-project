FEATURE: Realizar reservas
    AS um usuário   
    I WANT reservar uma acomodação 
    SO THAT eu possa me hospedar naquela acomodação 

SCENARIO: Realizar com sucesso uma reserva
    Given que o usuário comum de login “ymws” se encontra na página “Lista de Acomodações Disponíveis”
    And o usuário de login “ymws” consegue visualizar a lista de reservas disponíveis e a barra de pesquisa
    When o usuário de login “ymws” escolhe a acomodação “Hotel CIn”
    And o usuário de login “ymws” salva sua escolha
    Then o usuário de login “ymws” é redirecionado para a página de “Pagamento”
    And o usuário de login “ymws” preenche a forma de pagamento
    And o usuário de login “ymws” recebe a mensagem de “reserva confirmada”
    And o usuário de login “ymws” é redirecionado para a página de “Minhas reservas”

SCENARIO: Realizar uma reserva sem estar logado
    Given que o usuário comum não logado se encontra na página “Lista de Acomodações Disponíveis”
    And o usuário comum não logado consegue visualizar a lista de reservas disponíveis e uma barra de pesquisa
    When o usuário comum não logado escolhe a acomodação “Hotel CIn”
    And o usuário comum não logado seleciona a opção “salvar”
    Then o usuário comum não logado recebe uma mensagem “Você precisa estar logado para reservar uma acomodação”
    And o usuário comum não logado é redirecionado para a página de “Login”

SCENARIO: Visualizar todos os detalhes da acomodação
    Given que o usuário comum de login “ymws” se encontra na página “Lista de Acomodações Disponíveis"
    And o usuário comum de login "ymws" consegue visualizar a lista de reservas disponíveis e uma barra de pesquisa
    When o usuário comum de login “ymws” escolhe a acomodação “Hotel CIn”
    And o usuário comum de login “ymws” percebe que não tem todos os detalhes na tela
    Then o usuário comum de login "ymws" seleciona a opção "Hotel CIn"
    And o usuário comum de login "ymws" visualiza todos os detalhes disponíveis do "Hotel CIn"

SCENARIO: Adicionar Serviços Adicionais à Reserva
    Given que o usuário comum de login "ymws" está na página "Hotel CIn"
    And o usuário de login "ymws" visualiza informações detalhadas sobre a acomodação "Hotel CIn"
    When o usuário de login "ymws" seleciona a opção "Adicionar Serviços Adicionais"
    Then o usuário de login "ymws" é apresentado com uma lista de serviços adicionais
    And o usuário de login "ymws" escolhe "Café da manhã incluso" e "Vista para a praia"
    And o sistema atualiza o custo total da reserva com os serviços adicionais selecionados
    And o usuário de login "ymws" continua o processo de reserva com os serviços adicionais escolhidos