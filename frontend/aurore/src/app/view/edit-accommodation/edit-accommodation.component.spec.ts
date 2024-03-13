import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAccommodationComponent } from './edit-accommodation.component'

describe('EditAccommodationComponent', () => {
  let component: EditAccommodationComponent;
  let fixture: ComponentFixture<EditAccommodationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditAccommodationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditAccommodationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAccommodationComponent } from './edit-accommodation.component';

describe('EditAccommodationComponent', () => {
  let component: EditAccommodationComponent;
  let fixture: ComponentFixture<EditAccommodationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditAccommodationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditAccommodationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
