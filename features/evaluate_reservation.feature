
Scenario: adicionando nova avaliação

Given eu estou logo com usuario “Paulo”, email " paulo@gmail.com" e senha "123456"
And eu estou na pagina "Reservation History"
And eu fiz uma reserva no hotel “Dalhousie Castle” do dia “23/09/2023”
When eu adiciono “5 estrelas” para a reserva no hotel “Dalhousie Castle” do dia “23/09/2023”
And eu seleciono a opção “Salvar” 
Then eu ainda estou na pagina "Reservation History"
And eu posso ver no hotel “Dalhousie Castle” a avaliação “5 estrelas”

Scenario: ver avaliação no perfil do hotel

Given eu estou logado com usuario “qin”, email "qin@gmail.com" e senha "123456"
And eu estou na pagina "Reservation History"
And eu fiz uma avaliação para a reserva no hotel “Stanley Hotel” do dia “23/09/2023”
When eu mudo a pagina para “Stanley Hotel Profile”
Then eu posso ver minha avaliação para a reserva no hotel “Stanley Hotel” do dia “23/09/2023”
	
Scenario: adicionando nova avaliação mas não adicionando nenhuma estrela

Given eu estou logo com usuario “Robert”, email "robert@gmail.com" e senha "123456"
And eu estou na pagina "Reservation History"
And eu fiz uma reserva no hotel “Cecil hotel” do dia “23/09/2023”
When eu não adiciono nenhuma “estrela” para a reserva no hotel “Cecil hotel”
And eu adiciono “terrivel” no campo de comentário
And eu tento salvar as mudanças
Then eu ainda estou na pagina "Reservation History"
And a avaliação não é salva no sistema

Scenario: tento mudar uma avaliação minha

Given eu estou logado com usuario “Sara”, email "robert@gmail.com" e senha "123456"
And eu fiz uma avaliação para a reserva no hotel “Ahwahnee Hotel” do dia “30/02/2023”
When eu vou para a pagina "Reservation History"
And tento mudar minha avaliação para a reserva no hotel “Ahwahnee Hotel” do dia “30/02/2023”
Then eu não posso mudar qualquer parametro da avaliação


