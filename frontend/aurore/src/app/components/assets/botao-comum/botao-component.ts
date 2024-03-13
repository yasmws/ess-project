import { Component, OnInit, Input,  Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-botao',
  templateUrl: './botao.component.html',
  styleUrl: './botao.component.css'
})

export class BotaoComponent implements OnInit{
  @Input() rota: any; // recebe rota
  @Input() title: any;
  @Output() botaoClicado = new EventEmitter<void>();

  onClick(): void {
    this.botaoClicado.emit();
  }

  constructor(){}

  ngOnInit(): void {
      console.log("ROTA",this.rota)
  }
}