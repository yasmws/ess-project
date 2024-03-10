import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookAccommodationsComponent } from './book-accommodations.component';

describe('BookAccommodationsComponent', () => {
  let component: BookAccommodationsComponent;
  let fixture: ComponentFixture<BookAccommodationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BookAccommodationsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BookAccommodationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
