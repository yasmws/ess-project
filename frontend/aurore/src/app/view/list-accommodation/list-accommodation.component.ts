import { Component, Input, OnInit } from '@angular/core';
import {ManegementService} from '../../services/management/management.service'
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-list-accomodation',
    templateUrl: './list-accomodation.component.html',
    styleUrl: './list-accomodation.component.css'
})
export class ListAccomodationComponent implements OnInit{
    name: any;
    listAccommodation: any;
    titulo: any;
    showList: any;
    rota: any;
    rotaDel: any;
    loc: string = 'accomd';

    @Input() userName: any;

    constructor(private service: ManegementService,private route: ActivatedRoute){
        this.route.params.subscribe(params => {
            this.name = params['user'];
        });
    }

    ngOnInit(): void {
        if(this.name){
            console.log("NOME", this.name);

            this.service.getAccommodationList(this.name).subscribe((dados)=>{
                if(dados.detail){
                    this.listAccommodation = dados.detail;
                    console.log(this.listAccommodation)
                    this.titulo =  `${this.name} tem ${dados.detail.length} acomodações registradas`

                    if(dados.detail.length > 0){
                        this.rota = `/listAc/${this.name}/editAc`;
                        this.showList = true;
                        this.rotaDel = "accommodation";
                    }
                    else this.showList = false
                }
                else{
                    this.titulo =  `${this.name} não tem acomodações registradas`
                }
            });
        }
    }
}
