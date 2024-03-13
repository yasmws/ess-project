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

  sendRating(data:any): Observable<any>{
    const url = `http://localhost:8000/reservations/evaluate/${data.reservation_id}`;
    const params = new HttpParams()
      .set('reservation_id', data.reservation_id)
      .set('accommodation_id',data.accommodation_id)
      .set('stars', data.stars)
      .set('comment', data.comment);
    return this.http.post<any>(url, null, { params: params });
  }

  createUserPost(data:any): Observable<any>{
    const url = `http://localhost:8000/users/create`;
    const params = new HttpParams()
      .set('name', data.name)
      .set('username',data.username)
      .set('email', data.email)
      .set('cpf', data.cpf)
      .set('password', data.password);
    return this.http.post<any>(url, null, { params: params });
  }

  loginUserPost(data:any): Observable<any>{
    const url = `http://localhost:8000/users/login`;
    const params = new HttpParams()
      .set('emailOrUsername', data.emailOrUsername)
      .set('password', data.password);
    return this.http.post<any>(url, null, { params: params });
  }

  logoutUser(): Observable<any>{
    const url = `http://localhost:8000/users/logout`;
    return this.http.post<any>(url, null);
  }

  getLoggedUser(): Observable<any>{
    const url = `http://localhost:8000/users/logged`;
    return this.http.get<any>(url);
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

  createReservation(data: any): Observable<any> {
    const url = 'http://localhost:8000/reservation/create';

    const params = new HttpParams()
      .set('reservation_checkin', data.reservation_checkin)
      .set('reservation_checkout', data.reservation_checkout)
      .set('accommodation_id', data.accommodation_id)
      .set('client_id', data.client_id);

    console.log('Parameters:', params);

    return this.http.post<any>(url, null, { params });
  }
}

