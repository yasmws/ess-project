import { TestBed } from '@angular/core/testing';

import { ManegementService } from './management.service';

describe('ManegementService', () => {
  let service: ManegementService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ManegementService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
