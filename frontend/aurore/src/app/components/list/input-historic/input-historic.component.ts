import { Component , EventEmitter, Output} from '@angular/core';
import {FormControl, Validators} from '@angular/forms';


@Component({
  selector: 'app-input-historic',
  templateUrl: './input-historic.component.html',
  styleUrls: ['./input-historic.component.css']
})
export class InputHistoricComponent {

  checkInControl = new FormControl('', [Validators.required])
  checkOutControl = new FormControl('', [Validators.required])

  @Output() formSubmitted = new EventEmitter<{checkIn: string, checkOut: string, id: string}>();


  getErrorMessage(control: FormControl) {
    if (control.hasError('required')) {
      return 'Este campo é obrigatório*';
    }
    if(control.hasError('date')){
      return 'Data inválida*';
    }
    return '';
  }


  totalemDias(ano: number, mes: number, dia: number){

    let total = (mes * 30) +  dia + (ano * 12 * 30);
    return total;

  }



  showList(controlIn: FormControl, controlOut: FormControl){

    console.log("SHOW LIST:", controlIn.value, controlOut.value)
    let checkin = controlIn.value;
    let checkout = controlOut.value;

    let today : any = new Date();

    checkin = checkin.split('-');
    checkout =  checkout.split('-');

    today = this.totalemDias(today.getFullYear(),  today.getMonth() + 1,  today.getDate() );
    let checkIn =  this.totalemDias( Number(checkin[0]),  Number(checkin[1]),  Number(checkin[2]) );
    let checkOut = this.totalemDias(  Number(checkout [0]),   Number(checkout [1]),   Number(checkout [2]) );

    if(checkOut < checkIn){
      this.checkOutControl.setErrors({ 'date': true });
      this.checkInControl.setErrors({ 'date': true });
    }
    if(checkOut > today){
      this.checkOutControl.setErrors({ 'date': true });
    }
    if(checkIn > today){
      this.checkInControl.setErrors({ 'date': true });
    }

    if (this.checkInControl.valid && this.checkOutControl.valid) {
      console.log(this.checkInControl, this.checkOutControl);
      const checkInValue = `${checkin[0]}-${checkin[1]}-${checkin[2]}`;
      const checkOutValue =  `${checkout [0]}-${checkout[1]}-${checkout[2]}`;
      console.log(checkInValue, checkOutValue)

      this.formSubmitted.emit({checkIn: checkInValue.toString(), checkOut: checkOutValue.toString(), id: "pedro123"});
    }
  }
}
