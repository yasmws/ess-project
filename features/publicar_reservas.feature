FEATURE: Publicar reservas
    AS um usuário   
    I WANT compartilhar informações sobre as minhas acomodações disponíveis
    SO THAT outros usuários possam visualizar e eventualmente reservar essas acomodações

SCENARIO: Publicar uma reserva logado
    Given que o usuário com login “lmws” está na página de “Publicar uma reserva”
    When o usuário com login “lmws” preenche todas as informações de “dados obrigatórios”
    And o usuário com login “lmws” escolhe “publicar”
    Then o usuário com login “lmws” recebe uma mensagem de “reserva publicada”
    And o usuário com login “lmws” é redirecionado para a página “Minhas Publicações”

SCENARIO: Publicar uma reserva sem estar logado
    Given que o usuário não logado está na página de “Publicar uma reserva”
    When o usuário não logado preenche todas as informações de “dados obrigatórios”
    And o usuário não logado escolhe “publicar”
    Then o usuário não logado recebe uma mensagem “Você precisa estar logado para reservar uma acomodação”
    And o sistema limpa a página de “Publicar uma reserva”
    And o usuário é redirecionado para “Login”

SCENARIO: Editar uma reserva logado
    Given que o usuário com login “lmws” está na página de “Minhas Publicações”
    When o usuário com login “lmws” seleciona a opção "Editar uma reserva" 
    And o usuário com login “lmws” faz as alterações desejadas nas informações da acomodação "Hotel CIn"
    And o usuário com login “lmws” escolhe “Salvar alterações”
    Then o usuário com login “lmws” recebe uma mensagem de “Reserva atualizada com sucesso”
    And o usuário com login “lmws” é redirecionado de volta para a página “Minhas Publicações”
    And o usuário com login "lmws" pode checar suas edições
    
SCENARIO: Visualizar detalhes de uma reserva logado
    Given que o usuário com login “lmws” está na página de “Minhas Reservas”
    When o usuário com login “lmws” seleciona uma reserva específica da lista de suas reservas
    Then o usuário é redirecionado para a página de detalhes da reserva
    And o usuário pode visualizar "Data", "Acomodação", "Preço" e "Status da reserva"

SCENARIO: Excluir uma Reserva Publicada
    Given que o usuário com login "lmws" está na página "Minhas Publicações"
    And o usuário com login "lmws" visualiza a reserva que deseja excluir
    When o usuário com login "lmws" seleciona a opção "Excluir Reserva"
    And o sistema exibe uma mensagem de confirmação solicitando a confirmação do usuário para excluir a reserva
    And o usuário com login "lmws" confirma a exclusão
    Then o usuário com login "lmws" recebe uma mensagem de confirmação indicando que a reserva foi excluída com sucesso
    And o usuário com login "lmws" é redirecionado para a página "Minhas Publicações" atualizada, sem a reserva excluída.