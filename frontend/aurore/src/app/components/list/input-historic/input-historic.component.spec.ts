import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InputHistoricComponent } from './input-historic.component';

describe('InputHistoricComponent', () => {
  let component: InputHistoricComponent;
  let fixture: ComponentFixture<InputHistoricComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InputHistoricComponent]
    });
    fixture = TestBed.createComponent(InputHistoricComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
