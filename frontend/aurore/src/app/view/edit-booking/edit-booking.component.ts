import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder  } from '@angular/forms';
import { ManegementService } from '../../services/management/management.service'
import { ActivatedRoute , Router} from '@angular/router';

@Component({
    selector: 'app-edit-booking',
    templateUrl: './edit-booking.component.html',
    styleUrl: './edit-booking.component.css'
})
export class EditBookingComponent implements OnInit{
    registerForm: any = FormGroup;
    name: any; 
    alert: any;
    title: any;
    link: any ;
    disable: boolean = true;
    rota: any;
    id:any;
    accommodation:any;
    loc: string = "reserv";

    constructor(private fb: FormBuilder, private service: ManegementService,private route: ActivatedRoute, private router: Router){
    this.route.params.subscribe(params => {
        this.name = params['user'];
        this.id = params['id'];
        console.log("NAME E PARAM", this.name, this.id)
    });

    const navigation = this.router.getCurrentNavigation();
    if (navigation && navigation.extras.state) {
        this.accommodation  = navigation.extras.state['dados'].accommodation;
    }
}
@ViewChild('popUp') popUp!: ElementRef;

ngOnInit(): void {
    this.registerForm = this.fb.group({
        checkin: ['', [Validators.required], this.dateCheckinValidator.bind(this)],
        checkout: ['', [Validators.required], this.dateCheckoutValidator.bind(this)],
    });
}

totalemDias(ano: number, mes: number, dia: number){
    let total = (mes * 30) +  dia + (ano * 12 * 30);
    return total;
}

dateCheckinValidator(control: FormControl) {
    let today : any = new Date();
    let checkin = control.value.split('-');
    let checkout = this.registerForm.get('checkout').value

    checkout = checkout.split('-');
    today = this.totalemDias(today.getFullYear(),  today.getMonth() + 1,  today.getDate() );
    checkin =  this.totalemDias( Number(checkin[0]),  Number(checkin[1]),  Number(checkin[2]) );
    checkout = this.totalemDias(  Number(checkout [0]),   Number(checkout [1]),   Number(checkout [2]) );

    if (!control.value || isNaN(checkin)) {
        this.registerForm.get('checkin').setErrors({ 'invalidDate': true });
        return { invalidDate: true };
    }
    if(checkout && checkin >= checkout){
        this.registerForm.get('checkin').setErrors({ 'biggerCheckin': true });
        return { biggerCheckin: true };
    }
    if(checkin <= today){
        this.registerForm.get('checkin').setErrors({ 'invalidDate': true });
        return { invalidDate: true };
    }
    this.registerForm.get('checkin').setErrors({ 'valid': true });
    return null;
}

dateCheckoutValidator(control: FormControl) {
    console.log("Estou em checkout");

    let today : any = new Date();
    let checkout = control.value.split('-');
    let checkin = this.registerForm.get('checkin').value

    checkin = checkin.split('-');
    today = this.totalemDias(today.getFullYear(),  today.getMonth() + 1,  today.getDate() );
    checkin =  this.totalemDias( Number(checkin[0]),  Number(checkin[1]),  Number(checkin[2]) );
    checkout = this.totalemDias(  Number(checkout [0]),   Number(checkout [1]),   Number(checkout [2]) );

    console.log(today, checkin, checkout)

    if (!control.value || isNaN(checkout)) {
        this.registerForm.get('checkout').setErrors({ 'invalidDate': true });
        return { invalidDate: true };
    }
    if(checkin && checkin > checkout){
        console.log("ENTREI AQUI")
        this.registerForm.get('checkout').setErrors({ 'biggerCheckout': true });
        return { biggerCheckout: true };
    }
    if(checkout <= today){
        this.registerForm.get('checkout').setErrors({ 'invalidDate': true });
        return { invalidDate: true };
    }
    this.registerForm.get('checkout').setErrors({ 'valid': true });
    return null;
}

showPop(status: any){
    this.disable = false;

    if(status == 200){
        this.alert = "Obrigada, Sua reserva foi deletada com sucesso!"
        this.title = "Obrigada";
        this.link = '../../../assets/img/verificado.png';
        this.rota = '/'
        alert(this.alert)
    }
    else{
        this.alert = "Não foi possível editar sua reserva!"
        this.title = "Erro";
        this.link = '../../../assets/img/error.png';
        this.rota = '/'
        alert(this.alert)
    }
}

submitEdit(){
    let checkin = this.registerForm.get('checkin').value;
    let checkout = this.registerForm.get('checkout').value;
  
    const popUpElement = this.popUp.nativeElement as HTMLElement;
    this.title = "Um momento"
    this.alert = "Carregando informações"
    this.link = "../../../assets/img/carregando.png"
    popUpElement.style.visibility = 'visible';
      
    console.log("ACOMODATION_ID", this.accommodation)
    
    this.service.editReservation({
        id: this.id,
        checkin: checkin ,
        checkout: checkout,
        accommodation_id: this.accommodation,
        cliente_id: this.name
    }).subscribe((result)=>{
        if(result.status_code == 200){
            alert("Reserva editada com Sucesso!")
        }
        else{
            alert("Erro ao editar Reserva.")
        }
            this.router.navigateByUrl(`/listRs/${this.name}`);
    })
}}
