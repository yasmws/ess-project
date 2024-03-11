import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

interface Accommodation {
  id: string;
  name: string;
  description: string;
  bedrooms: number;
  location: string;
  max_capacity: number;
  image: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  accommodations: Accommodation[] = [];

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit(): void {
    this.fetchAccommodations();
  }

  fetchAccommodations(): void {
    const url = 'http://localhost:8000/accommodation/list';
    this.http.get<Accommodation[]>(url).subscribe(data => {
      this.accommodations = data;
    });
  }

  navigateToAccommodationDetails(id: string): void {
    this.router.navigate(['/accommodation', id]);
  }
}
