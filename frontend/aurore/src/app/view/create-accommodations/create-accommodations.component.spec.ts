import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateAccommodationsComponent } from './create-accommodations.component';

describe('CreateAccommodationsComponent', () => {
  let component: CreateAccommodationsComponent;
  let fixture: ComponentFixture<CreateAccommodationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateAccommodationsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CreateAccommodationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
