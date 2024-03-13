import { Component, Input } from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';
import { ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})

export class RatingComponent {
  
  name:any = "error";
  loc:string = "menu";
  @Input() reservation_id!:string;
  @Input() accommodation_id!: string;
  stars!:number;
  comment!:string;

  constructor(private serviceMngt: ManegementService, private route: ActivatedRoute, private location: Location){
    this.route.params.subscribe(params => {
      this.reservation_id = params['reserva'];
      this.accommodation_id = params['accomodation'];
      this.name = params['user'];
      console.log(this.reservation_id)
      this.route.params.subscribe(params => {
        });
      });

    
  }
 

  onChangeStars($event:number){
    this.stars = $event;
  }

  sendRating(){

    var data ={
      reservation_id:  this.reservation_id,
      accommodation_id: this.accommodation_id,
      stars: this.stars,
      comment: this.comment,
    }

    if(this.stars > 0){
      this.serviceMngt.sendRating(data).subscribe({
        next: (res:any)=>{
          console.log(res,'response')},
        error: (err:any)=>{
          console.log(err, 'error')
        }
      });
      
      this.location.back();
    }

  }

}
