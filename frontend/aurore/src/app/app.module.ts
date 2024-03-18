import { NgModule} from '@angular/core';
import { CommonModule} from '@angular/common';

import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component';
import { RoutingModule } from './app.routing.module';// Import RouterModule
import { HttpClientModule } from '@angular/common/http';

import {HistoricComponent} from './components/list/historic/historic.component'
import {InputHistoricComponent} from './components/list/input-historic/input-historic.component'
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatToolbarModule} from '@angular/material/toolbar';

import { RatingComponent } from './components/rating/rating.component';
import { StarsComponent } from './components/stars/stars.component';
import {FormBuilder, FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { EditBookingComponent } from './view/edit-booking/edit-booking.component';
import { ListReservationComponent } from './view/list-reservation/list-reservation.component';
import { ListAccomodationComponent } from './view/list-accommodation/list-accommodation.component';
import { EditAccommodationComponent  } from './view/edit-accommodation/edit-accommodation.component';
import { HistoricMainComponent } from './view/historic-main/historic-main.component';
import { BotaoComponent } from './components/assets/botao-comum/botao-component';
import { CardComponent } from './components/card/card.component';
import { HeaderComumComponent } from './components/headers/header-comum/header-comum.component';
import { ListCardComponent } from './components/list_card/list-card.component';
import { CreateAccommodationsComponent } from './view/create-accommodations/create-accommodations.component';
import { BookAccommodationsComponent } from './view/book-accommodations/book-accommodations.component';

import {HeaderHomeComponent } from './components/headers/header-home/header-home.component'
import { EmailComponent} from './components/email/email.component'
import { SearchPageComponent } from './search-page/search-page.component';


@NgModule({
  declarations: [
    AppComponent,
    RatingComponent,
    BookingMngtComponent,
    HistoricComponent,
    InputHistoricComponent,
    BotaoComponent,
    EditBookingComponent,
    HeaderComumComponent,
    ListReservationComponent,
    ListAccomodationComponent,
    CardComponent,
    ListCardComponent,
    HistoricMainComponent,
    EditAccommodationComponent ,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    HeaderHomeComponent,
    CreateAccommodationsComponent,
    BookAccommodationsComponent,
    EmailComponent,
    SearchPageComponent
  ],
  imports: [
    StarsComponent,
    BrowserModule,
    RoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    CommonModule,
    MatIconModule,
    MatInputModule,
    MatFormFieldModule,
    MatToolbarModule,
    FormsModule,
    ReactiveFormsModule,
    FontAwesomeModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
