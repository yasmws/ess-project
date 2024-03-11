import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { HomeComponent } from './home/home.component';
import { RatingComponent } from './components/rating/rating.component';

const routes: Routes = [
  { path: '', redirectTo: '/search', pathMatch: 'full' },
  { path: 'search', component: SearchPageComponent},
  { path: 'booking-mngt', component:  BookingMngtComponent },
  { path: 'historic/rating', component:  RatingComponent },
  { path: 'home', component: HomeComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RoutingModule { }