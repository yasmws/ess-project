import { Component , EventEmitter, OnInit, Output} from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import { ManegementService } from '../../services/management/management.service';


@Component({
  selector: 'app-book-accommodations',
  templateUrl: './book-accommodations.component.html',
  styleUrl: './book-accommodations.component.css'
})

export class BookAccommodationsComponent implements OnInit{
    id: any;
    route: any;
    accommodationInfo: any;
   
    // Modifica cor do botão
    buttonColor = "#8C271E";
    changeButtonColor(color: string): void {
    this.buttonColor = color;
    }

    constructor(private service: ManegementService) {}

    // Recebe os dados do back
    ngOnInit(): void {
      // Retrieve the 'id' parameter from the route
      //this.route.params.subscribe((params: { [x: string]: any; }) => {
      //  this.id = params['id'];
      //  console.log("ID:", this.id);
        this.id = "5f834504-53b1-48df-9dec-c5beaa3b9dd5";
        
        this.service.getUrlImg(this.id).subscribe((dados: any) => { //NotFound
            console.log("Recebendo dados do back...", dados);
            this.accommodationInfo.append(dados)
        });

        this.service.getAcmdtInfo(this.id).subscribe((dados: any) => {
          console.log("Recebendo dados do back...", dados);
          // Armazenar os dados recebidos p exibição no template
          
          this.accommodationInfo = dados
          console.log(this.accommodationInfo)
        });
    };
}

    
 
