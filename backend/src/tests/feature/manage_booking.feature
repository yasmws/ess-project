
Feature: Gerenciamento acomodação API

Scenario: Editar reserva com check-out menor que check-in

    Given Uma reserva de id "09424fe7-6c69-4eca-b3ab-6afe6dafa682", existe no bando de dados
    When um usuário envia uma requisição PUT para "/reservation/09424fe7-6c69-4eca-b3ab-6afe6dafa682/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-21",cliente "yasmin123", acomodação "09424fe7-6c69-4eca-b3ab-6afe6dafa682" e reserva "0132eade-6776-4a09-8f49-9b461e981d2b"
    Then o status do código deve ser "400"
    And o Json de resposta deve conter "Invalid fields"

Scenario: Deletar reserva que não existe

    Given Uma reserva de id "d5aabe0e-afd6-4a6e-8f03-b972fede4d63", não existe no bando de dados
    When um usuário envia uma requisição DELETE para "/reservation/d5aabe0e-afd6-4a6e-8f03-b972fede4d63/delete" 
    Then o status do código deve ser "404"
    And o Json de resposta deve conter "A Reserva não existe no banco de dados"


Scenario: Editar reserva com sucesso

    Given Uma reserva de id "09424fe7-6c69-4eca-b3ab-6afe6dafa682", existe no bando de dados
    When um usuário envia uma requisição PUT para "/reservation/09424fe7-6c69-4eca-b3ab-6afe6dafa682/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-26", cliente "pedro123", acomodação "45922c44-8277-4682-b2a7-04e8cffaadd6" e reserva "09424fe7-6c69-4eca-b3ab-6afe6dafa682"
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Reservation updated successfully!"

Scenario: Editar reserva com acomodação inexistente

    Given Uma reserva de id "09424fe7-6c69-4eca-b3ab-6afe6dafa682", existe no bando de dados
    When um usuário envia uma requisição PUT para "/reservation/09424fe7-6c69-4eca-b3ab-6afe6dafa682/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-24", cliente "pedro123", acomodação "be7cf4d8-f408-42-92b5be751c4" e reserva "09424fe7-6c69-4eca-b3ab-6afe6dafa682"
    Then o status do código deve ser "400"
    And o Json de resposta deve conter "Invalid fields"

Scenario: Deletar reserva com sucesso

    Given Uma reserva de id "e5542777-0b92-4fb9-b8e9-7fd95cb82445", existe no bando de dados
    When um usuário envia uma requisição DELETE para "/reservation/e5542777-0b92-4fb9-b8e9-7fd95cb82445/delete" 
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Reserva deletada com sucesso!"
    And a reserva de id "e5542777-0b92-4fb9-b8e9-7fd95cb82445" não está mais disponível 


    


    