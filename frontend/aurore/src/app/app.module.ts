import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' }, // Default route redirects to /home
  { path: 'home', component: HomeComponent },
  // Add more routes for other components/pages as needed
];
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent
  ],

  imports: [
  BrowserModule,
  RouterModule.forRoot(
    routes)
  ],

  providers: [],

  bootstrap: [AppComponent]
})
export class AppModule { }
