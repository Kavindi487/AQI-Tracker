import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { AqiService } from '../../service/aqi.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule, NavbarComponent],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  city = 'Colombo';
  cities = ['Colombo', 'Kandy', 'Galle'];

  pm25: number | null = null;
  co: number | null = null;
  no2: number | null = null;

  aqi: number | null = null;
  label = '—';
  advice = '';
  loading = false;
  error = '';

  constructor(private aqiService: AqiService) {}

  predictAQI() {
    this.error = '';
    this.loading = true;

    if (this.pm25 === null || this.co === null || this.no2 === null) {
      this.error = 'Please fill all fields.';
      this.loading = false;
      return;
    }

    this.aqiService.predict({
      city: this.city,
      pm25: this.pm25,
      co: this.co,
      no2: this.no2
    }).subscribe({
      next: (res) => {
        this.aqi = res.aqi;
        this.label = res.category;
        this.advice = res.advice;
        this.loading = false;
      },
      error: (err) => {
        this.error = err?.error?.error || 'Prediction failed.';
        this.loading = false;
      }
    });
  }
}