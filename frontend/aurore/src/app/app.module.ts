import { NgModule} from '@angular/core';
import { CommonModule} from '@angular/common';

import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { BookingMngtComponent } from './view/booking-mngt/booking-mngt.component';
import { RoutingModule } from './app.routing.module';// Import RouterModule
import { HttpClientModule } from '@angular/common/http';

import {HistoricComponent} from './components/list/historic/historic.component'
import {InputHistoricComponent} from './components/list/input-historic/input-historic.component'
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';

import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HomeComponent } from './home/home.component';


@NgModule({
  declarations: [
    AppComponent,
    BookingMngtComponent,
    HistoricComponent,
    InputHistoricComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    RoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    CommonModule,
    MatIconModule,
    MatInputModule,
    MatFormFieldModule,
    FormsModule, 
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
