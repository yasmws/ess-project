import { Component } from '@angular/core';
import {ManegementService} from '../../services/management/management.service'
import {ActivatedRoute} from '@angular/router'

@Component({
    selector: 'app-historic-main',
    templateUrl: './historic-main.component.html',
    styleUrl: './historic-main.component.css'
})

export class HistoricMainComponent {
    name:any;
    loc: string = "reserv";

    constructor(private serviceMngt: ManegementService, private route: ActivatedRoute){

        this.route.params.subscribe(params => {
        this.name = params['user'];
        });
    }

    historicData: any;

    ngOnInit(): void {}
    onFormSubmitted(formData: { checkIn: string, checkOut: string }) {
        this.historicData = formData;
    }
}
