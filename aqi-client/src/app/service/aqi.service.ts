import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PredictRequest {
  city: string;
  pm25: number;
  co: number;
  no2: number;
}

export interface PredictResponse {
  aqi: number;
  category: string;
  advice: string;
  inputs: PredictRequest;
}

@Injectable({
  providedIn: 'root'
})
export class AqiService {
  private apiUrl = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {}

  predict(data: PredictRequest): Observable<PredictResponse> {
    return this.http.post<PredictResponse>(`${this.apiUrl}/predict`, data);
  }
}