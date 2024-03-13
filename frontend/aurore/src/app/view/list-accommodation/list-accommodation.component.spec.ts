import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAccomodationComponent } from './list-accomodation.component';

describe('ListAccomodationComponent', () => {
  let component: ListAccomodationComponent;
  let fixture: ComponentFixture<ListAccomodationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListAccomodationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListAccomodationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
