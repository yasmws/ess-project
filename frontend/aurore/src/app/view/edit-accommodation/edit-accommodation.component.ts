import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ManegementService } from 'src/app/services/management/management.service';

@Component({
  selector: 'app-edit-accommodation',
  templateUrl: './edit-accommodation.component.html',
  styleUrl: './edit-accommodation.component.css'
})
export class EditAccommodationComponent implements OnInit {
  editForm:any;
  name: any;
  id:any;
  loc: string = 'accomd';

  constructor(private fb: FormBuilder, private route: ActivatedRoute, private service: ManegementService,  private rt: Router){
    this.route.params.subscribe(params => {
      this.name = params['user'];
      this.id = params['id'];
    });
  }

  ngOnInit(): void {
    this.editForm = this.fb.group({
      name: [''],
      location: [''],
      bedrooms: [''],
      maxCapacity: [''],
      description: ['']
    });
  }

  editaAcmd(): void {

    let dados = this.editForm.value;
    console.log("dados do form:", dados)
    
    this.service.editAccommodation({
      id: this.id,
      name: dados.name,
      location: dados.location,
      bedrooms: dados.bedrooms,
      max_capacity: dados.maxCapacity,
      description: dados.description,
    }).subscribe((dados)=>{
      alert(dados.detail)
      this.rt.navigateByUrl(`/listAc/${this.name}`);
    })

  }
}
