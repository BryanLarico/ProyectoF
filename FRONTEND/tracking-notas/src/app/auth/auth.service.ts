import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrlSignUP = 'http://127.0.0.1:8000/api/users/';
  private apiUrlLogin = 'http://127.0.0.1:8000/api/auth/';

  constructor(private http: HttpClient) {}

  login(userData: UserLogin): Observable<any> {
    return this.http.post(this.apiUrlLogin, userData);
  }

  signup(userData: UserData): Observable<any> {
    return this.http.post(this.apiUrlSignUP, userData)
  }
}
interface UserData {
  username: string,
  password: string,
  email: string,
}

interface UserLogin {
  username: string,
  password: string,
}