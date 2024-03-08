import { Component, OnInit, Input} from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';

@Component({
  selector: 'app-historic',
  templateUrl: './historic.component.html',
  styleUrls: ['./historic.component.css'],
})

export class HistoricComponent implements OnInit {

  constructor(private serviceMngt: ManegementService){}

  dadosList: any;
  
  @Input() historicData: any; 



  ngOnInit(): void {

    console.log("DADOS RECEBIDOS", this.historicData);

    
    
    this.serviceMngt.getHistoryc({
      id: this.historicData.id, 
      checkin: this.historicData.checkIn,
      checkout: this.historicData.checkOut
    }).subscribe((dados:any)=>{
      this.dadosList = dados.detail;
      console.log("HISTORICO")
      console.log(this.dadosList)
    });
  }

}
