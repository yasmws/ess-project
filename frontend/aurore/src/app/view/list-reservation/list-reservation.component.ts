import { Component, Input, OnInit } from '@angular/core';
import { ManegementService } from '../../services/management/management.service'
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-list-reservation',
    templateUrl: './list-reservation.component.html',
    styleUrl: './list-reservation.component.css'
})
export class ListReservationComponent {
    name: any;
    listReservation: any;
    titulo: any;
    showList: any;
    rota: any;
    rotaDel: any;
    loc: string = "reserv";
    historic: any;


    constructor(private service: ManegementService, private route: ActivatedRoute) {

        this.route.params.subscribe(params => {
            this.name = params['user'];
            console.log("AQUI, TESTANDO", this.name);
            this.historic = `/listRs/${this.name}/historic`
        });

    }
    ngOnInit(): void {
        this.service.getReservationList(this.name).subscribe((dados) => {
            console.log(dados);
            if (dados.detail) {
                this.listReservation = dados.detail;
                console.log(this.listReservation);
                this.titulo = `${this.name} tem ${dados.detail.length} reservas confirmadas`
                if (dados.detail.length > 0) {
                    this.rota = `/listRs/${this.name}/editRs`;
                    this.rotaDel = "reservation";
                    this.showList = true;
                }
                else this.showList = false
            }
        });
    }
}
