Feature: Create reservations

    Creating the reservations and posting them in the db
# Some accommodation_id's that exist in our db
# f7f863a6-ab1a-459f-935f-c3b2bcc55734
# 02a68c9e-0a90-45ce-b455-b4d1056122e4
# 02b17782-8981-4f75-ad53-d5261c83fc57

Scenario: Criar uma reserva de uma acomodação existente com sucesso
    Given existe uma acomodação com accommodation_id "02b17782-8981-4f75-ad53-d5261c83fc57" no banco de dados
    When uma requisição POST for enviada para "/reservation/create" com os dados da reserva nos campos: checkin: "2024-09-01", checkout: "2024-09-02", client_id: "pedro123", accommodation_id: "02b17782-8981-4f75-ad53-d5261c83fc57"
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Reservation created successfully!"

Scenario: Criar uma reserva de uma acomodação inexistente
    Given não existe uma acomodação com id "Yasminmws"
    When uma requisição POST for enviada para "/reservation/create" com os dados da reserva nos campos: checkin: "2024-09-03", checkout: "2024-09-04", client_id: "pedro123", accommodation_id: "Yasminmws"
    Then o status da resposta a ser mostrada é "404"
    And a resposta deve conter a mensagem "Accommodation not found"

Scenario: Criar uma reserva com cliente inexistente no banco de dados
    Given não existe um cliente cuja id é "lucinda456"
    When uma requisição POST for enviada para "/reservation/create" com os dados da reserva nos campos: checkin: "2024-09-05", checkout: "2024-09-06", client_id: "lucinda456", accommodation_id: "45922c44-8277-4682-b2a7-04e8cffaadd6"
    Then o status da resposta a ser mostrada é "404"
    And a resposta deve conter a mensagem "Client not found"

Scenario: Criar uma reserva com data de checkin depois da data de checkout 
    Given existe uma acomodação com accommodation_id "45922c44-8277-4682-b2a7-04e8cffaadd6" no banco de dados
    When uma requisição POST for enviada para "/reservation/create" com os dados da reserva nos campos: checkin: "2024-07-18", checkout: "2024-07-10", client_id: "pedro123", accommodation_id: "45922c44-8277-4682-b2a7-04e8cffaadd6"
    Then o status da resposta a ser mostrada é "400"
    And a resposta deve conter a mensagem "Check-out date must be after check-in date"

Scenario: Criar uma reserva de um cliente cuja id é a mesma daquele que criou a acomodação
    Given existe uma acomodação com accommodation_id "45922c44-8277-4682-b2a7-04e8cffaadd6" no banco de dados e aquele que criou a acomodação tem id "yasmin123"
    When uma requisição POST for enviada para "/reservation/create" com os dados da reserva nos campos: checkin: "2024-07-10", checkout: "2024-07-12", client_id: "yasmin123", accommodation_id: "45922c44-8277-4682-b2a7-04e8cffaadd6"
    Then o status da resposta a ser mostrada é "400"
    And a resposta deve conter a mensagem "Client cannot reserve their own accommodation"

Scenario: Criar uma reserva com, pelo menos, uma das datas escolhidas indisponíveis
    Given existe uma acomodação com accommodation_id "45922c44-8277-4682-b2a7-04e8cffaadd6" no banco de dados
    When uma requisição POST for enviada para "/reservation/create" com os dados da reserva nos campos: checkin: "2024-07-13", checkout: "2024-07-17", client_id: "pedro123", accommodation_id: "45922c44-8277-4682-b2a7-04e8cffaadd6"
    Then o status da resposta a ser mostrada é "400"
    And a resposta deve conter a mensagem "Chosen date already reserved"


