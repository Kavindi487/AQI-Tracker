import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface AqiResponse {
  aqi: number;
  category: string;
  advice: string;
  inputs: {
    city: string;
    pm25: number;
    co: number;
    no2: number;
  };
}

@Injectable({
  providedIn: 'root'
})
export class AqiService {
  private apiUrl = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {}

  predict(payload: {
    city: string;
    pm25: number;
    co: number;
    no2: number;
  }): Observable<AqiResponse> {
    return this.http.post<AqiResponse>(`${this.apiUrl}/predict`, payload);
  }
}