import { Component, ElementRef, Input, OnChanges, SimpleChanges, ViewChild} from '@angular/core';

@Component({
  selector: 'app-list-card',
  templateUrl: './list-card.component.html',
  styleUrls: ['./list-card.component.css']
})
export class ListCardComponent implements OnChanges {
  @ViewChild('reservaList')reservaList!: ElementRef;

  @Input() reservas: any;
  @Input() showList: any;
  @Input() rota: any;
  @Input() rotaDel: any;

  constructor() {}

  ngOnChanges(changes: SimpleChanges): void {
    if (this.reservas) {

      let reserva = this.reservaList.nativeElement as HTMLElement;
      if (this.showList) {
        reserva.style.visibility = 'visible';
      } else {
        reserva.style.visibility = 'hidden';
      }
    } else {
      console.log("reservas é indefinido");
    }
  }
}
