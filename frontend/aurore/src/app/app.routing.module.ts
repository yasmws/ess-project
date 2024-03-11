import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component';
import { CreateAccommodationsComponent} from './view/create-accommodations/create-accommodations.component'
import { BookAccommodationsComponent } from './view/book-accommodations/book-accommodations.component';
import { PaymentComponent } from './view/payment/payment.component';
import { MyReservationsComponent} from './view/my-reservations/my-reservations.component'
import { MyAccommodationsComponent} from './view/my-accommodations/my-accommodations.component'

const routes: Routes = [
  { path: '', component:  BookingMngtComponent },
  { path: 'create-acmdt', component:  CreateAccommodationsComponent },
  { path: 'book-acmdt', component:  BookAccommodationsComponent },
  { path: 'payment', component: PaymentComponent},
  { path: 'my-reservations', component: MyReservationsComponent},
  { path: 'my-accommodations', component: MyAccommodationsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RoutingModule { }