import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { any } from 'cypress/types/bluebird';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.css']
})
export class SearchPageComponent {
  errorMessage: any;
  constructor(private http: HttpClient, private router: Router) { }

  searchAccommodations(): void {
    const baseUrl = 'http://localhost:8000/accommodation/list';
    const location = (document.getElementById('location') as HTMLInputElement).value;
    const checkin = (document.getElementById('checkin') as HTMLInputElement).value;
    const checkout = (document.getElementById('checkout') as HTMLInputElement).value;
    const guests = (document.getElementById('guests') as HTMLInputElement).value;

    let url = baseUrl + '?';
    if (location) url += `location=${location}&`;
    if (checkin) url += `checkin=${checkin}&`;
    if (checkout) url += `checkout=${checkout}&`;
    if (guests) url += `guests=${guests}&`;

    const headers = new HttpHeaders({
      'Accept': 'application/json'
    });

    this.http.get(url, { headers }).subscribe((data: any) => {
      console.log(data);
      if (Array.isArray(data)) {
        this.router.navigate(['/home'], {
          queryParams: {
            checkin,
            checkout
          }
        });
      }
      else {
        this.errorMessage = (data as any).message;
      }
    });
  }

  onSearchClick(): void {
    this.searchAccommodations();
  }
}
