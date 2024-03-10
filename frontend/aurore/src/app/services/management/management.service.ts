import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';

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

  sendRating(data:any): Observable<any>{
    const url = `http://localhost:8000/reservations/evaluate/${data.reservation_id}`;
    const params = new HttpParams()
      .set('reservation_id', data.reservation_id)
      .set('accommodation_id',data.accommodation_id)
      .set('stars', data.stars,)
      .set('comment', data.comment);
    return this.http.post<any>(url, null, { params: params });
  }
  
}
