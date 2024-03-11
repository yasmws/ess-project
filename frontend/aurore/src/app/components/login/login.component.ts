import { Component } from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private serviceMngt: ManegementService){}

  emailOrUsername!: string
  password!: string

  loginUser(){
    var inputData = {
      emailOrUsername: this.emailOrUsername,
      password: this.password,
    }

    this.serviceMngt.loginUserPost(inputData).subscribe({
      next: (res:any)=>{
        console.log(res,'response')},
      error: (err:any)=>{
        console.log(err, 'error')
      }
    });
  }
}
