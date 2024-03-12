
// Import necessary modules and decorators
import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ManegementService } from '../../services/management/management.service';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
class ImageSnippet {
  constructor(public src: string, public file: File) {}
}
@Component({
  selector: 'app-create-accommodations',
  templateUrl: './create-accommodations.component.html',
  styleUrls: ['./create-accommodations.component.css']
})

export class CreateAccommodationsComponent implements OnInit {

  constructor(
    private snackBar: MatSnackBar,
    private router: Router,
    private formBuilder: FormBuilder,
    private service: ManegementService,
    private http: HttpClient) { }


  // Modificar cor do botão
  buttonColor = "#8C271E";
  changeButtonColor(color: string): void {
  this.buttonColor = color;
  }
  
  accommodationForm!: FormGroup;
  
  data: any;
  accommodation_name: string = '';
  accommodation_loc: string = '';
  accommodation_bedrooms: number = 0;
  accommodation_max_capacity: number = 0;
  accommodation_description: string = '';
  accommodation_price: number = 0;
  accommodation_id: string = '';
  user_id: string = 'pedro123';

  ngOnInit(): void {
    this.accommodationForm = this.formBuilder.group({
      accommodation_name: ['', [Validators.required, this.validateNameLength.bind(this)]],
      accommodation_loc: ['', Validators.required],
      accommodation_bedrooms: [0, [Validators.required, Validators.min(1), this.validatePositiveInteger.bind(this)]],
      accommodation_max_capacity: [0, [Validators.required, Validators.min(1), this.validatePositiveInteger.bind(this)]],
      accommodation_description: ['', [Validators.required, this.validateDescriptionLength.bind(this)]],
      accommodation_price: [0, [Validators.required, Validators.min(0)]],
    });
  }

  hasError(controlName: string, errorType: string): boolean {
    const control = this.accommodationForm.get(controlName);
    return control?.hasError(errorType) || false;
  }
  
  // Validação dos dados
  validateNameLength(control: AbstractControl): { [key: string]: any } | null {
    const name = control.value;
    if (name && name.length > 20) {
      return { 'nameLengthExceeded': true };
    }
    return null;
  }

  validatePositiveInteger(control: AbstractControl): { [key: string]: any } | null {
    const value = control.value;
    if (!Number.isInteger(value) || value <= 0) {
      return { 'notPositiveInteger': true };
    }
    return null;
  }

  validateDescriptionLength(control: AbstractControl): { [key: string]: any } | null {
    const description = control.value;
    if (description && description.length > 400) {
      return { 'descriptionLengthExceeded': true };
    }
    return null;
  }


  createAcmdt(): void {
    console.log("resultado:",this.accommodationForm.valid)
    if (this.accommodationForm.valid) {
      this.data = {
        accommodation_name: this.accommodationForm.value.accommodation_name,
        accommodation_loc: this.accommodationForm.value.accommodation_loc,
        accommodation_bedrooms: this.accommodationForm.value.accommodation_bedrooms,
        accommodation_max_capacity: this.accommodationForm.value.accommodation_max_capacity,
        accommodation_description: this.accommodationForm.value.accommodation_description,
        accommodation_price: this.accommodationForm.value.accommodation_price,
        user_id: this.user_id
      };
    }

    console.log("dados:",this.data);
    this.service.createAccommodation(this.data).subscribe((dados)=>{ 
      this.accommodation_id = dados.detail;
      console.log("recebendo dados do back...");
      
      // Exibe o pop-up de sucesso
      this.snackBar.open('Accommodation created successfully!', 'Close', {
        duration: 10000, // Duração em milissegundos
        horizontalPosition: 'center',
        verticalPosition: 'top',
      });

      // Navega para 'my-accommodations'
      this.router.navigate(['/my-accommodations']);
    });


    //Img
    /*
    handleFileInput(event: any): void {
      const file = event.target.files[0];
  
      if (file) {
        const reader = new FileReader();
    

    if (this.accommodationForm.value.accommodation_img) {
      const formData = new FormData();
      formData.append('accommodation_img', this.accommodationForm.value.accommodation_img);
      formData.append('accommodation_id', this.accommodation_id);
  
      this.service.createAccommodationImg(formData).subscribe((dados) => {
        console.log("recebendo dados do back...", dados);
      });
    }*/
    
  }
}

