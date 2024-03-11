import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search-page',
  standalone: true,
  imports: [],
  templateUrl: './search-page.component.html',
  styleUrl: './search-page.component.css'
})
export class SearchPageComponent {
  location: string = '';

  constructor(private router: Router) { }

  searchAccommodations(): void {
    // Redirecionar para a página Home
    this.router.navigate(['/home']);
  }
}