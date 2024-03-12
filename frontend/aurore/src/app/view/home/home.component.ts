import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  constructor(private router: Router) {}

  redirectToBookAcmdt(): void {

    const dataToPass = {
      reservation_checkin: '2024-05-20',
      reservation_checkout: '2024-05-22', 
      accommodation_id: '5f834504-53b1-48df-9dec-c5beaa3b9dd5', 
      client_id: 'brenow', 
    };
   
    this.router.navigate(['/book-acmdt'], { state: { data: dataToPass }});
  }
}
