import { Component, Input } from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';
import { ActivatedRoute,Router} from '@angular/router';
import { Location } from '@angular/common';
@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})

export class RatingComponent {

  accommodation: any;
  reservation:any;
  name: any;
  loc: string = 'reserv';

  constructor(private serviceMngt: ManegementService, private route: ActivatedRoute, private rt: Router, private location: Location){

    this.route.params.subscribe(params => {
      this.name = params['user'];
    });
    
     const navigation = this.rt.getCurrentNavigation();
     this.accommodation= navigation!.extras.state!['accommodation'];
     this.reservation = navigation!!.extras.state!['reservation']

  }


  @Input() reservation_id!:string;
  @Input() accommodation_id!: string;
  stars!:number;
  comment!:string;

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
