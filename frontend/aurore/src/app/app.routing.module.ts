import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component'
import { CreateAccommodationsComponent} from './view/create-accommodations/create-accommodations.component'
import { BookAccommodationsComponent } from './view/book-accommodations/book-accommodations.component';

const routes: Routes = [
  { path: '', component:  BookingMngtComponent },
  { path: 'create-acmdt', component:  CreateAccommodationsComponent },
  { path: 'book-acmdt', component:  BookAccommodationsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RoutingModule { }