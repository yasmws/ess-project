import { Component, OnInit, Input, ViewChild, ElementRef, EventEmitter, Output} from '@angular/core';
import {ActivatedRoute} from '@angular/router'
import { ManegementService } from 'src/app/services/management/management.service';
@Component({
  selector: 'app-header-comum',
  templateUrl: './header-comum.component.html',
  styleUrl: './header-comum.component.css'
})
export class HeaderComumComponent implements OnInit{

  constructor(private route: ActivatedRoute, private service: ManegementService){

  }

  @ViewChild('menu') menuPop!: ElementRef;
  @ViewChild('accomod') accomod!: ElementRef;
  @ViewChild('reserv') reserv!: ElementRef;

  @Output()

  rotaA: any;
  rotaB: any;
  menu: boolean = true;
  visible: any = false;
  clicked: boolean = false;

  name: any = true;
  valid: boolean = false;

  @Input() userName : any;
  @Output() parametroEnviado = new EventEmitter<string>();
  @Input() loc: any;

  ngOnInit(): void {

    this.service.getLoggedUser().subscribe((result)=>{
      if(result){
        console.log("nome aqui", result)
        this.name = false;
        this.userName = result
        this.valid = true;
      }
    })

  }

  showMenu(){
   console.log("click triggered");
   const popUpElement =  this.menuPop.nativeElement as HTMLElement;
   this.visible = !this.visible;

   if(this.visible){
    popUpElement.style.visibility = 'visible';
   }
   else{
    popUpElement.style.visibility = 'hidden';
   }

  }

  logOut(){
    console.log("AQUII")
    this.service.logoutUser();
    window.location.reload();
  }

  changeClick(){
    this.clicked = !this.clicked;
  }

  accodation(){
   this.rotaA = `/listAc/${this.userName}`
  }

  reservation(){
    this.rotaB = `/listRs/${this.userName}`
  }
}
