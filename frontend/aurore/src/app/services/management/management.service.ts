import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { NONE_TYPE } from '@angular/compiler';

@Injectable({
  providedIn: 'root'
})
export class ManegementService {

  constructor(private http: HttpClient) { }


  getHistoryc(data:any): Observable<any>{
    return this.http.get<any>(`http://localhost:8000/historyc/${data.id}`, { params: { id: data.id, checkin: data.checkin, checkout: data.checkout } });
  }

  getUrlImg(id:string): Observable<any>{
    return this.http.get<any>(`http://localhost:8000/accommodation/${id}/image`, { params: { id: id} });
  }

  getAccommodationList(id:string): Observable<any>{
    return this.http.get<any>(`http://localhost:8000/accommodations/${id}/list`, { params: { id: id}});
  }

  getReservationList(id:string): Observable<any>{
    return this.http.get<any>(`http://localhost:8000/reservations/${id}/list`, { params: { id: id}});
  }

  editReservation(data: any): Observable<any> {
    const url = `http://localhost:8000/reservation/${data.id}/edit`;
    const params = new HttpParams()
      .set('checkin_date', data.checkin)
      .set('checkout_date', data.checkout)
      .set('accommodation_id', data.accommodation_id)
      .set('cliente_id', data.cliente_id);

    return this.http.put<any>(url, null, { params: params });
  }

  editAccommodation(data: any): Observable<any> {

    const url = `http://localhost:8000/accommodation/${data.id}/edit`;
    const params = new HttpParams()
      .set('name', data.name  )
      .set('location', data.location )
      .set('bedrooms', data.bedrooms)
      .set('max_capacity', data.max_capacity)
      .set('description', data.description );
    return this.http.put<any>(url, null, { params: params });
  }


  deleteId(rota:string): Observable<any>{
    console.log(rota)
    return this.http.delete(`http://localhost:8000/${rota}`);
  }
}
