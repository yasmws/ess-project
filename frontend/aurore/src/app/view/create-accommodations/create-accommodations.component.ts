import { Component , EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import { fromEvent } from 'rxjs';
import { FormBuilder  } from '@angular/forms';
import { ManegementService } from '../../services/management/management.service';

@Component({
  selector: 'app-create-accommodations',
  templateUrl: './create-accommodations.component.html',
  styleUrl: './create-accommodations.component.css'
})

export class CreateAccommodationsComponent {

  constructor(private service:ManegementService){}

  /* Muda a cor do botão quando clica-se nele*/
  buttonColor: string = '#8C271E';
  changeButtonColor(): void{
    this.buttonColor = '#38354E'
  }

  accommodation_name: string = '';
  accommodation_loc: string = '';
  accommodation_bedrooms: number = 0;
  accommodation_max_capacity: number = 0;
  accommodation_description: string = '';
  accommodation_price: number = 0;
  user_id: string = 'pedro123';
  //user_id!:string;

  createAcmdt(){
    var data ={
      accommodation_name: this.accommodation_name,
      accommodation_loc: this.accommodation_loc,
      accommodation_bedrooms:  this.accommodation_bedrooms,
      accommodation_max_capacity: this.accommodation_max_capacity,
      accommodation_description: this.accommodation_description,
      accommodation_price: this.accommodation_price,
      user_id: this.user_id 
    }
    console.log(data)
    this.service.createAccommodation(data).subscribe({
      next: (res:any)=>{
        console.log(res,'response')},
      error: (err:any)=>{
        console.log(err, 'error')
      }
    });
  }
  
  /*ngOnInit(): void {
    console.log("aaa")
    this.service.createAccommodation({
      accommodation_name: 'Lugar Bonito',
      accommodation_loc: 'Recife',
      accommodation_bedrooms:  2,
      accommodation_max_capacity: 4 ,
      accommodation_description: 'A beautiful place in Recife',
      accommodation_price: 1000,
      user_id: 'pedro123'
    }).subscribe((dados) => {
      console.log(dados)
    })
  }*/
}
  //@Input

