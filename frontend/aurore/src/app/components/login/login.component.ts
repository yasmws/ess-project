import { Component } from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';
import {Router} from '@angular/router'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private serviceMngt: ManegementService, private route: Router){}

  emailOrUsername!: string
  password!: string

  erro: string = ""

  openSuccessLogin(){
    document.getElementById("success-login")!.style.display = "block";
  }

  loginUser(){
    var inputData = {
      emailOrUsername: this.emailOrUsername,
      password: this.password,
    }

    this.serviceMngt.loginUserPost(inputData).subscribe({
      next: (res:any)=>{
        this.openSuccessLogin();
        //this.route.navigateByUrl('/home')
        console.log(res)},
      error: (err:any)=>{
        this.erro = err.error.detail
        console.log(this.erro)
      }
    });
  }

}
