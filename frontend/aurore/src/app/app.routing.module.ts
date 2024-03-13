import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { HomeComponent } from './home/home.component';
import { RatingComponent } from './components/rating/rating.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { ListAccomodationComponent } from './view/list-accommodation/list-accommodation.component';
import { ListReservationComponent } from './view/list-reservation/list-reservation.component';
import { HistoricMainComponent } from './view/historic-main/historic-main.component';
import { EditBookingComponent } from './view/edit-booking/edit-booking.component';
import { EditAccommodationComponent } from './view/edit-accommodation/edit-accommodation.component';
import { CreateAccommodationsComponent } from './view/create-accommodations/create-accommodations.component';
import { BookAccommodationsComponent } from './view/book-accommodations/book-accommodations.component';
import { EmailComponent} from './components/email/email.component'
// import { ListReservationComponent } from './view/list-reservation/list-reservation.component';
// import { HistoricMainComponent } from './view/historic-main/historic-main.component';
// import { EditBookingComponent } from './view/edit-booking/edit-booking.component';
// import { EditAccommodationComponent } from './view/edit-accommodation/edit-accommodation.component';

const routes: Routes = [
  { path: '', redirectTo: '/search', pathMatch: 'full' },
  { path: 'search', component: SearchPageComponent},
  { path: 'booking-mngt', component:  BookingMngtComponent },
  { path: 'historic/rating', component:  RatingComponent },
  { path: 'home', component: HomeComponent  },
  { path: 'users/create', component: RegisterComponent, title: 'Register'},
  { path: 'users/login', component: LoginComponent, title: 'Login'},
  { path: 'listAc/:user', component:ListAccomodationComponent},
  { path: 'listRs/:user', component:ListReservationComponent},
  { path: 'listRs/:user/historic', component: HistoricMainComponent},
  { path: 'listRs/:user/editRs/:id', component: EditBookingComponent },
  { path: 'listAc/:user/editAc/:id', component: EditAccommodationComponent},
  { path: 'listRs/:user/rating', component: RatingComponent},
  { path: 'create-acmdt', component: CreateAccommodationsComponent},
  { path: 'book-acmdt', component: BookAccommodationsComponent},

  // { path: 'listAc/:user', component:ListAccomodationComponent},
  // { path: 'listRs/:user', component:ListReservationComponent},
  // { path: 'listRs/:user/historic', component: HistoricMainComponent},
  // { path: 'listRs/:user/editRs/:id', component: EditBookingComponent },
  // { path: 'listAc/:user/editAc/:id', component: EditAccommodationComponent},
  // { path: 'listRs/:user/historic/:id', component: RatingComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RoutingModule { }
