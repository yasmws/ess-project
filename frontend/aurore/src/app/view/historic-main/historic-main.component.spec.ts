import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistoricMainComponent } from './historic-main.component';

describe('HistoricMainComponent', () => {
  let component: HistoricMainComponent;
  let fixture: ComponentFixture<HistoricMainComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HistoricMainComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(HistoricMainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
