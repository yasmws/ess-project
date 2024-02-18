
Feature: Editar reseva 


Scenario: Editar reseva por data
    Given Uma reserva de id "0132eade-6776-4a09-8f49-9b461e981d2b", existe no bando de dados reservations
    When um usuário envia uma requisição "POST" para "/reservation/0132eade-6776-4a09-8f49-9b461e981d2b/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-24", cliente "yasmin123", acomodação "02a68c9e-0a90-45ce-b455-b4d1056122e4 e reserva "0132eade-6776-4a09-8f49-9b461e981d2b"
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Reservation updated successfully!"


