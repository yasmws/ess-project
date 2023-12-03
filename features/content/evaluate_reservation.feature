
Scenario: adicionando nova avaliação

Given eu estou logado com usuario “Paulo”
And eu estou na pagina "Reservation History"
When eu adiciono “5 estrelas” para a reserva no hotel “Dalhousie Castle”
And eu salvo as mudanças
Then eu estou na pagina "Reservation History"
And eu posso ver no hotel “Dalhousie Castle” a avaliação “5 estrelas”

Scenario: ver avaliação no perfil do hotel

Given eu estou logado com usuario “qin”
And eu estou na pagina "Reservation History"
And eu fiz uma avaliação para a reserva no hotel “Stanley Hotel” do dia em “23/09/2023”
When eu mudo a pagina para “Stanley Hotel Profile”
Then eu posso ver minha avaliação para a reserva no hotel “Stanley Hotel” em “23/09/2023”
	
Scenario: adicionando nova avaliação mas não adicionando nenhuma estrela

Given eu estou logado com usuario “Robert”
And eu estou na pagina "Reservation History"
When eu não adiciono nenhuma “estrela” para a reserva no hotel “Cecil hotel”
And eu adiciono “terrivel” no campo de comentário
And eu tento salvar as mudanças.
Then eu ainda estou na pagina "Reservation History"
And a avaliação não é salva no sistema

Scenario: tento mudar uma avaliação minha

Given eu estou logado com usuario “Sara”
And eu fiz uma avaliação para a reserva no hotel “Ahwahnee Hotel” do dia em “30/02/2023”
When eu vou para a pagina "Reservation History"
And tento mudar minha avaliação para a reserva no hotel “Ahwahnee Hotel” do dia em “30/02/2023”
Then eu não posso mudar qualquer parametro da avaliação


