import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookingMngtComponent } from './booking-mngt.component';

describe('BookingMngtComponent', () => {
  let component: BookingMngtComponent;
  let fixture: ComponentFixture<BookingMngtComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BookingMngtComponent]
    });
    fixture = TestBed.createComponent(BookingMngtComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
