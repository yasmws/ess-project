import { Component } from '@angular/core';
import { ManegementService } from 'src/app/services/management/management.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  
  constructor(private serviceMngt: ManegementService){}

  name!: string
  username!: string
  email!: string
  cpf!: string
  password!: string

  createUser(){
    var inputData = {
      name: this.name,
      username: this.username,
      email: this.email,
      cpf: this.cpf,
      password: this.password,
    }

    this.serviceMngt.createUserPost(inputData).subscribe({
      next: (res:any)=>{
        console.log(res,'response')},
      error: (err:any)=>{
        console.log(err, 'error')
      }
    });
  }
}
