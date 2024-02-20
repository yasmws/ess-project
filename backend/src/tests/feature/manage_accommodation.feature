Feature: Gerenciamento de acomodação API

Scenario: Editar acomodação com sucesso

    Given Uma acomodação de id "71176949-333b-452a-86a8-d79eeda1abd5", existe no bando de dados
    When um usuário envia uma requisição PUT para "/accommodation/71176949-333b-452a-86a8-d79eeda1abd5/edit" com as seguintes infromações, descrição "Luxo, Glamuor", max_capacity "30"
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Acomodação editada com sucesso!"

Scenario: Editar acomodação com campos inválidos

    Given Uma acomodação de id "6c8739ad-5bbe-49b8-95a4-5ef59ae9ca95", existe no bando de dados
    When um usuário envia uma requisição PUT para "/accommodation/6c8739ad-5bbe-49b8-95a4-5ef59ae9ca95/edit" com as seguintes infromações, location "Belo Horizonte", name "Casa de jujuba"
    Then o status do código deve ser "404"
    And o Json de resposta deve conter "Campos inválidos"





