import { Component , EventEmitter, Output} from '@angular/core';
import {FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-book-accommodations',
  templateUrl: './book-accommodations.component.html',
  styleUrl: './book-accommodations.component.css'
})
export class BookAccommodationsComponent{

    buttonColor: string = '#8C271E';
    changeButtonColor(): void{
      this.buttonColor = '#38354E'
    }
    
}
