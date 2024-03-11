import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent implements OnInit {
  data: any;

  constructor(private router: Router, private http: HttpClient) {}

  ngOnInit(): void {
    const navigation = this.router.getCurrentNavigation();
    if (navigation && navigation.extras && navigation.extras.state) {
      this.data = navigation.extras.state['data'];
      console.log('Data received on the payment page:', this.data);
    }
  }

  // Ação quando clica no botão
  dataReserva: any;
  createReservation(): void {
    if (this.data && this.data.valid) {
      const dataReserva = {
        reservation_checkin: this.data.checkin,
        reservation_checkout: this.data.checkout,
        accommodation_id: this.data.accommodation_id,
        client_id: this.data.client_id
      };
  
      // Convert dataReserva into URL parameters
      const params = new HttpParams({ fromObject: dataReserva });
  
      this.http
        .get<any>('http://localhost:8000/reservation/create', { params })
        .pipe(
          catchError((error) => {
            console.error('Error creating reservation:', error);
            throw error;
          })
        )
        .subscribe({
          next: (result) => {
            alert('Reserva criada com sucesso!');
            console.log('Result:', result);
  
            const goToHome = confirm('Deseja ir para a página inicial?');
            if (goToHome) {
              this.router.navigate(['/']);
            } else {
              this.router.navigate(['/my-reservations']);
            }
          },
          error: (error) => {
            console.error('Error creating reservation:', error);
          }
        });
    } else {
      console.error('Data is undefined or does not have the valid property.');
    }   
  }
}
