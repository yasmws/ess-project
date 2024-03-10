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
      .set('nome', data.accommodation_name)
      .set('loc', data.accommodation_loc)
      .set('num_quartos', data.accommodation_bedrooms)
      .set('max_capacidade', data.accommodation_max_capacity)
      .set('descricao', data.accommodation_description)
      .set('preco', data.accommodation_price)
      .set('user_id', data.user_id);

    return this.http.post<any>(url, null, { params: params });
  }
  
}
