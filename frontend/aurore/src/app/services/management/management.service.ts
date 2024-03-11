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
  
}
