import { Component, OnInit, Input, ViewChild, ElementRef, EventEmitter, Output} from '@angular/core';
import {ActivatedRoute} from '@angular/router'
@Component({
  selector: 'app-header-comum',
  templateUrl: './header-comum.component.html',
  styleUrl: './header-comum.component.css'
})
export class HeaderComumComponent implements OnInit{

  constructor(private route: ActivatedRoute){
    this.route.params.subscribe(params => {
      console.log("RESELTADO DOS PARAMETROS",params);
    });
  }

  @ViewChild('menu') menuPop!: ElementRef;
  @ViewChild('accomod') accomod!: ElementRef;
  @ViewChild('reserv') reserv!: ElementRef;
  @ViewChild('create') create!: ElementRef;

  @Output()

  rotaA: any;
  rotaB: any;
  rotaC: any;
  menu: boolean = true;
  visible: any = false;
  clicked: boolean = false;

  @Input() userName : any;
  @Output() parametroEnviado = new EventEmitter<string>();
  @Input() loc: any;

  ngOnInit(): void {

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

  changeClick(){
    this.clicked = !this.clicked;
  }

  accodation(){
   this.rotaA = `/listAc/${this.userName}`
  }

  reservation(){
    this.rotaB = `/listRs/${this.userName}`
  }

  createAcmdt(){
    this.rotaC = '/createAcmdt'
  }
}
