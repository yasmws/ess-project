import { ManegementService } from 'src/app/services/management/management.service';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { catchError } from 'rxjs/operators';
import { HttpParams } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs/internal/Observable';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrl: './payment.component.css'
})
export class PaymentComponent implements OnInit {
  data: any;

  constructor(private route: ActivatedRoute, private router: Router, private http: HttpClient, private service: ManegementService){
    // Recupera os dados passados pela rota
    const navigation = this.router.getCurrentNavigation();
    if (navigation && navigation.extras && navigation.extras.state) {
      this.data = navigation.extras.state['data'];
      console.log('Data received from previous page:', this.data);
    }
  }

  ngOnInit(): void {
    // Check if 'data' is defined
    if (!this.data) {
      console.error('Data is undefined.');
    }
  }
  
 
}

