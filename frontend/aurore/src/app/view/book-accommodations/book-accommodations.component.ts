import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ManegementService } from '../../services/management/management.service';

@Component({
  selector: 'app-book-accommodations',
  templateUrl: './book-accommodations.component.html',
  styleUrl: './book-accommodations.component.css'
})
export class BookAccommodationsComponent implements OnInit {
  id: any;
  accommodationInfo: any;
  data: any;
  name: any;
  loc: any = 'pass';

  constructor(private route: ActivatedRoute, private router: Router, private service: ManegementService) {
    const navigation = this.router.getCurrentNavigation();
    if (navigation) {
      this.data = navigation.extractedUrl["queryParams"];
      console.log('Data received from previous page:', this.data);
    }
  }

  ngOnInit(): void {
    this.name = this.service.getLoggedUser()
    this.service.getAcmdtInfo(this.data['accommodation_id']).subscribe((dados: any) => {
      console.log("Recebendo dados do back...", dados);
      // Armazenar os dados recebidos para exibição no template
      this.accommodationInfo = dados;
      console.log(this.accommodationInfo);
    });
  }

  // Modifica cor do botão
  buttonColor = "#8C271E";

  changeButtonColor(color: string): void {
    this.buttonColor = color;
  }

  // Rota do botão
  onButtonClick(): void {
    const data = this.data
    data['client_id'] = this.service.getLoggedUser()
    console.log('Enviando os seguintes dados para pagamento:', data)
    this.router.navigate(['/payment'], { state: { data } });
  }
}
