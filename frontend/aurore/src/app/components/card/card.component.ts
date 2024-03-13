import { Component, Input, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { ManegementService } from 'src/app/services/management/management.service';
import { Location } from '@angular/common';
@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrl: './card.component.css'
})
export class CardComponent {
  @Input() reserva: any;
  @Input() rota: any;
  @Input() rotaDel: any;
  rotaEdit: any;

  constructor(private router: Router, private service: ManegementService, private location: Location){}

  rotaChange(): void {
    if (this.reserva && this.rota) {
      const rotaEdit = `${this.rota}/${this.reserva.id}`;
  
      const dados = {
        accommodation: this.reserva.accommodation_id
      };

      this.router.navigate([rotaEdit], { state: { dados } });
    }
  }

  deleteCard(){
    if(this.reserva && this.rotaDel){

      const confirmacao = window.confirm("Você deseja deletar esta moradia?");

      if(confirmacao){

        const url = `${this.rotaDel}/${this.reserva.id}/delete`

        this.service.deleteId(url).subscribe((result)=>{
          alert(result.detail);
          window.location.reload();
          
        });

      }
     
    }
  }
}