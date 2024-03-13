import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderComumComponent } from './header-comum.component';

describe('HeaderComumComponent', () => {
  let component: HeaderComumComponent;
  let fixture: ComponentFixture<HeaderComumComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderComumComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(HeaderComumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
