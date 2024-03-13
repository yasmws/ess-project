import { Component, OnInit, Input} from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';
import { ActivatedRoute, Router} from "@angular/router"

@Component({
  selector: 'app-historic',
  templateUrl: './historic.component.html',
  styleUrls: ['./historic.component.css'],
})

export class HistoricComponent implements OnInit {
  dadosList: any;
  user:any;
  id:any;

  constructor(private serviceMngt: ManegementService, private route: ActivatedRoute, private rt: Router){
     this.route.params.subscribe(params => {
      this.user = params['user'];
      console.log(this.user)
    });
  }

  @Input() historicData: any;



  ngOnInit(): void {
    this.serviceMngt.getHistoryc({
      id: this.historicData.id,
      checkin: this.historicData.checkIn,
      checkout: this.historicData.checkOut
    }).subscribe((dados:any)=>{
      console.log("RESULTADOS",dados)
      this.dadosList = dados.detail;
    });
  }

  routerTest(dado:any){

    const url = `/listRs/${this.user}/rating`
    this.rt.navigate([url], { state: { accommodation: `${dado.accommodation_id}`, reservation: `${dado.reservation_id}`} });
  }

}
