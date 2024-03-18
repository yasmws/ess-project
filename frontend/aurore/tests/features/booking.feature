Feature: Reservar acomodação
Como um usuário
Eu quero reservar uma acomodação
Para poder garantir minha estadia

Scenario: Reservar uma acomodação com sucesso
Given O usuário "pedro123" está logado e na página de pesquisa "/search"
When O usuário clica no botão de busca
And O usuário é redirecionado para a página "/home"
And O usuário clica na primeira acomodação disponível
And O usuário é redirecionado para a página de "/book-acmdt"
And O usuário clica no botão "Reservar"
Then O usuário deve ser redirecionado para a página de "/pagamento"

Scenario: Reservar uma acomodação sem selecionar uma acomodação
Given O usuário "pedro123" está logado e na página de pesquisa "/book-acmdt"
And O usuário é redirecionado para a página de "/book-acmdt"
When O usuário clica no botão "Reservar"
Then O usuário deve ser redirecionado para a página de "/home"
And O formulário não é enviado
