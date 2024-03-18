Feature: Criar acomodação
Como um usuário
Eu quero criar uma acomodação
Para que outro usuário possa reservá-la

Scenario: Criar acomodação com sucesso
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "4", descrição: "This is a nice place to stay!", preco: "150"
And Eu clico no botão "Salvar"
Then Eu devo ser redirecionado para "/home"

Scenario: Criar acomodação com campo obrigatório não preenchido
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "4", descrição: "This is a nice place to stay!", preco: ""
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação

Scenario: Criar acomodação com número de hóspedes menor que o número de quartos
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "1", descrição: "This is a nice place to stay!", preco: ""
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação

Scenario: Criar acomodação com preço negativo
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "4", descrição: "This is a nice place to stay!", preco: "-50"
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação

Scenario: Criar acomodação com descrição muito longa
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "4", descrição: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae bibendum nisi, id consequat dui. Suspendisse potenti. Phasellus id libero tincidunt, tempus odio sit amet, vulputate ligula. Morbi id orci at ipsum varius congue at et nisl. Donec id suscipit dui. Nullam nec ante enim. Nullam quis ex nec eros tempus maximus. Mauris eget nisi neque. Sed sit amet massa libero. Fusce euismod pharetra magna sit amet scelerisque. In feugiat eros vitae felis laoreet, ac bibendum odio molestie. In tempor leo vel odio fermentum, ac bibendum ipsum vehicula. Curabitur in ligula in nulla gravida vehicula a id felis. Suspendisse eu efficitur quam. Sed maximus leo non libero faucibus interdum. Vivamus vitae justo ac est venenatis aliquam nec eget libero. Suspendisse potenti. Phasellus nec vestibulum velit. Sed posuere nulla ac suscipit tempus. Aenean non felis leo. In eu lobortis nulla. Fusce nec bibendum enim, id eleifend nisi. Sed sit amet varius libero. Aliquam sed mi nec turpis venenatis lacinia nec a purus. Quisque sed nulla ac nisi dictum dignissim non vitae tortor. Morbi et felis eget metus volutpat ullamcorper vel ac lacus.", preco: "150"
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação

Scenario: Criar acomodação com número máximo de hóspedes igual ao número de quartos
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "2", descrição: "This is a nice place to stay!", preco: "150"
And Eu clico no botão "Salvar"
Then Eu devo ser redirecionado para "/home"

Scenario: Tentar criar acomodação com nome muito longo
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation with a very long name that exceeds the maximum allowed length", localização: "Nice", num de quartos: "2", capacidade máxima: "4", descrição: "This is a nice place to stay!", preco: "150"
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação

Scenario: Tentar criar acomodação com número de quartos inválido (zero)
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "0", capacidade máxima: "4", descrição: "This is a nice place to stay!", preco: "150"
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação

Scenario: Tentar criar acomodação com capacidade máxima inválida (zero)
Given O usuário "pedro123" está logado e na página de criar acomodação "create-acmdt"
When Eu preencho os detalhes da acomodação com nome: "My accommodation", localização: "Nice", num de quartos: "2", capacidade máxima: "0", descrição: "This is a nice place to stay!", preco: "150"
And Eu tento clicar no botão "Salvar"
Then Eu devo não ser capaz de criar a acomodação
