Feature: Disparar email com comprovante de pagamento

    As a usuário
    I want to receber comprovante de pagamento de reserva por email
    so that eu posso verificar que meu pagamento foi sucedido

    Scenario: Disparo de comprovante por email
        Given eu estou logado como usário de nome "Lucy", email "songbird@tomail.com" e senha "m0ck1ngj4y"
        And eu estou na página "Lista de acomodações disponíveis"
        And eu seleciono "Salvar reserva"
        When eu efetuo pagamento da reserva
        Then o sistema gera um arquivo de nome "transacao-efetuada.pdf"
        And o sistema envia o arquivo "transacao-efetuada.pdf" por email para "songbird@tomail.com"
        