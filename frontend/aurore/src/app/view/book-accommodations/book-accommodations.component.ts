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

  constructor(private route: ActivatedRoute, private router: Router, private service: ManegementService) {
    // Recupera os dados passados pela rota
    const navigation = this.router.getCurrentNavigation();
    if (navigation && navigation.extras && navigation.extras.state) {
      this.data = navigation.extras.state['data'];
      console.log('Data received from previous page:', this.data);
    }
  }

  ngOnInit(): void {
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
    console.log('Enviando os seguintes dados para pagamento:', data)
    this.router.navigate(['/payment'], { state: { data } });
  }
}
