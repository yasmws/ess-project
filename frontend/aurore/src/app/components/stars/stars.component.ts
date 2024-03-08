import { Component, Input, Output, EventEmitter } from '@angular/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { CommonModule } from '@angular/common';
import { faStar } from '@fortawesome/free-solid-svg-icons/faStar';

@Component({
  selector: 'app-stars',
  templateUrl: './stars.component.html',
  imports: [FontAwesomeModule, CommonModule],
  standalone: true,
  styleUrls: ['./stars.component.css']
})
export class StarsComponent {
  faStar = faStar;
  @Output() changeStars:EventEmitter<number> = new EventEmitter<number>();
  stars: number = 0;
  
  setStarNumber(value: number){
    this.stars = value
    this.changeStars.emit(this.stars)
  }

}
