
Feature: Gerenciamento acomodação API


Scenario: Editar reserva com sucesso

    Given Uma reserva de id "0132eade-6776-4a09-8f49-9b461e981d2b", existe no bando de dados
    When um usuário envia uma requisição PUT para "/reservation/0132eade-6776-4a09-8f49-9b461e981d2b/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-24", cliente "yasmin123", acomodação "02a68c9e-0a90-45ce-b455-b4d1056122e4" e reserva "0132eade-6776-4a09-8f49-9b461e981d2b"
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Reservation updated successfully!"

Scenario: Editar reserva com acomodação inexistente

    Given Uma reserva de id "0132eade-6776-4a09-8f49-9b461e981d2b", existe no bando de dados
    When um usuário envia uma requisição PUT para "/reservation/0132eade-6776-4a09-8f49-9b461e981d2b/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-24", cliente "yasmin123", acomodação "be7cf4d8-f408-41e7-85f2-920b5be751c4" e reserva "0132eade-6776-4a09-8f49-9b461e981d2b"
    Then o status do código deve ser "404"
    And o Json de resposta deve conter "Não existe reserva para acomodação Castelo dos Sonhos"

Scenario: Editar reserva com check-out menor que check-in

    Given Uma reserva de id "b57ebbc4-c9e9-4783-8103-10f75685f06a", existe no bando de dados
    When um usuário envia uma requisição PUT para "/reservation/b57ebbc4-c9e9-4783-8103-10f75685f06a/edit" com as seguintes infromações data de check-in "2024-02-22", data de check-out "2024-02-21", cliente "yasmin123", acomodação "be7cf4d8-f408-41e7-85f2-920b5be751c4" e reserva "0132eade-6776-4a09-8f49-9b461e981d2b"
    Then o status do código deve ser "400"
    And o Json de resposta deve conter "Invalid fields"


Scenario: Deletar reserva com sucesso
    Given Uma reserva de id "705f7c92-a158-467e-a6e7-e9bea9cffc4b", existe no bando de dados
    When um usuário envia uma requisição DELETE para "/reservation/705f7c92-a158-467e-a6e7-e9bea9cffc4b/delete" 
    Then o status do código deve ser "200"
    And o Json de resposta deve conter "Reserva deletada com sucesso!"
    And a reserva de id "705f7c92-a158-467e-a6e7-e9bea9cffc4b" não está mais disponível 


Scenario: Deletar reserva que não existe

    Given Uma reserva de id "d5aabe0e-afd6-4a6e-8f03-b972fede4d63", não existe no bando de dados
    When um usuário envia uma requisição DELETE para "/reservation/d5aabe0e-afd6-4a6e-8f03-b972fede4d63/delete" 
    Then o status do código deve ser "404"
    And o Json de resposta deve conter "A Reserva não existe no banco de dados"
    


    





