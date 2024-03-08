import { Component, Input } from '@angular/core';
import { StarsComponent } from '../stars/stars.component';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})
export class RatingComponent {
  @Input() reservation_id:string = "q";
  @Input() accommodation_id: string ="q";
  @Input() stars:number = 0;

  onChangeStars(stars:number){
    this.stars = stars
  }

  
 /* @Input() component!: string
  @Input() flag = 0
  

  constructor(reservaton_id:string, accommodation_id:string){
    this.reservation_id = reservaton_id
    this.accommodation_id = accommodation_id
  } */

}
