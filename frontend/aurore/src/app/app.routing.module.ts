import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component'
import { RatingComponent } from './components/rating/rating.component';

const routes: Routes = [
  { path: '', component:  BookingMngtComponent },
  { path: 'historic/rating', component:  RatingComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RoutingModule { }