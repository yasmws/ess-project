Feature: Avaliar reserva serviço

Scenario: Nenhuma estrela foi adicionada
    Given o formulário foi preenchido com os dados em reservation_id = “1e3476a2-09a6-4669-b48b-6c271550d38b” e accommodation_id = “be7cf4d8-f408-41e7-85f2-920b5be751c4” e stars = “0” e comment = "esse"
    When uma requisição post foi enviada para /reservations/"1e3476a2-09a6-4669-b48b-6c271550d38b"/evaluate
    Then o sistema retorna o status code "500" e a mesagem “the number of stars is not in the allowed range.”

Scenario: Mais estrelas do que o permitido
    Given o formulário foi preenchido com os dados em reservation_id = “27637f28-d831-49f0-a136-78ea3967eada” e accommodation_id = “a019fe5d-9a96-4bb1-8cfb-e7c38b612244” e stars = “12” e comment = "ala"
    When uma requisição post foi enviada para /reservations/"27637f28-d831-49f0-a136-78ea3967eada"/evaluate
    Then o sistema retorna o status code "500" e a mesagem “the number of stars is not in the allowed range.”

Scenario: enviar avaliação para reserva
    Given o formulário foi preenchido com os dados em reservation_id = “dd8b7fc5-9113-48e9-b487-47881a8a3b92” e accommodation_id = “be7cf4d8-f408-41e7-85f2-920b5be751c4” e stars = “3” e comment = "ovo"
    When uma requisição post foi enviada para /reservations/"dd8b7fc5-9113-48e9-b487-47881a8a3b92"/evaluate
    Then o sistema retorna a mesagem “User rating added successfully!”

Scenario: enviar avaliação, mas a avaliação já existe para aquela reserva
    Given o formulário foi preenchido com os dados em reservation_id = “0132eade-6776-4a09-8f49-9b461e981d2b” e accommodation_id = “02a68c9e-0a90-45ce-b455-b4d1056122e4” e stars = “4” e comment = "salas"
    When uma requisição post foi enviada para /reservations/"3d231446-61da-4e41-b25f-d20d171e6be6"/evaluate
    Then o sistema retorna o status code "500" e a mesagem “it already has an evaluation in rating table”
