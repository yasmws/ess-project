Feature: Gerenciamento de acomodação API

Scenario: Excluir acomodação sem reserva

    Given Uma acomodação de id "6c8739ad-5bbe-49b8-95a4-5ef59ae9ca95", existe no bando de dados
    When um usuário envia uma requisição DELETE para "/accommodation/6c8739ad-5bbe-49b8-95a4-5ef59ae9ca95/delete" 
    Then o status do código deve ser "400"
    And o Json de resposta deve conter "Não se pode deletar acomodações com reservas"

Scenario: Editar acomodação com sucesso

    Given Uma acomodação de id "d5aabe0e-afd6-4a6e-8f03-b972fede4d63", existe no bando de dados
    When um usuário envia uma requisição PUT para "/accommodation/d5aabe0e-afd6-4a6e-8f03-b972fede4d63/edit" com as seguintes infromações, descrição "Xuxuzinho, Glamuor", max_capacity "30"
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Acomodação editada com sucesso!"

Scenario: Editar acomodação com campos inválidos

    Given Uma acomodação de id "45922c44-8277-4682-b2a7-04e8cffaadd6", existe no bando de dados
    When um usuário envia uma requisição PUT para "/accommodation/45922c44-8277-4682-b2a7-04e8cffaadd6/edit" com as seguintes infromações, location "Belo Horizonte", name "Casa de jujuba"
    Then o status do código deve ser "400"
    And o Json de resposta deve conter "Campos inválidos"

Scenario: Excluir acomodação sem reserva

    Given Uma acomodação de id "6c8739ad-5bbe-49b8-95a4-5ef59ae9ca95", existe no bando de dados
    When um usuário envia uma requisição DELETE para "/accommodation/6c8739ad-5bbe-49b8-95a4-5ef59ae9ca95/delete" 
    Then o status do código deve ser "400"
    And o Json de resposta deve conter "Não se pode deletar acomodações com reservas"