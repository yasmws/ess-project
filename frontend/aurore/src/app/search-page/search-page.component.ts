// search-page.component.ts

import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.css']
})
export class SearchPageComponent {
  constructor(private http: HttpClient, private router: Router) { }

  searchAccommodations(): void {
    const url = 'http://localhost:8000/accommodation/list';
    const headers = new HttpHeaders({
      'Accept': 'application/json'
    });

    this.http.get(url, { headers }).subscribe((data: any) => {
      console.log(data); // Aqui você pode fazer algo com os dados da resposta, se necessário
      this.router.navigate(['/home']);
    });
  }
}
