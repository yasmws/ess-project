import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ManegementService {

  constructor(private http: HttpClient) { }


  getHistoryc(data:any): Observable<any>{
    console.log("DATA", data);
    return this.http.get<any>(`http://localhost:8000/historyc/${data.id}`, { params: { id: data.id, checkin: data.checkin, checkout: data.checkout } });
  }

  getUrlImg(id:string): Observable<any>{
    return this.http.get<any>(`http://localhost:8000/accommodation/${id}/image`, { params: { id: id} });
  }

  getAcmdtInfo(id: string): Observable<any> {
    return this.http.get<any>(`http://localhost:8000/accommodation/${id}` , {params: {id: id} });    
  }

  createAccommodation(
    data:any
  ): Observable<any> {
    const url = 'http://localhost:8000/accommodation/create';

    const params = new HttpParams()
      .set('accommodation_name', data.accommodation_name)
      .set('accommodation_loc', data.accommodation_loc)
      .set('accommodation_bedrooms', data.accommodation_bedrooms)
      .set('accommodation_max_capacity', data.accommodation_max_capacity)
      .set('accommodation_description', data.accommodation_description)
      .set('accommodation_price', data.accommodation_price)
      .set('user_id', data.user_id);
    
    console.log('parametros:', params)

    return this.http.post<any>(url, null, { params: params });
  }

  createAccommodationImg(
    data:any
  ): Observable<any>{
    const url = 'http://localhost:8000/accommodation/create/upload_img'
    
    const params = new HttpParams()
      .set('accommodation_id', data.accommodation_id)
      .set('file', data.accommodation_img);

    console.log('paramentros (img):', params)

    return this.http.post<any>(url, null, { params: params});
  }
}
