import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { AqiService, PredictResponse } from '../../service/aqi.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule, NavbarComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  city = 'Colombo';
  pm25: number | null = null;
  co: number | null = null;
  no2: number | null = null;

  aqi = 0;
  label = '-';
  advice = 'Air quality category is estimated based on entered pollutant levels.';
  loading = false;
  error = '';

  constructor(private aqiService: AqiService) {}

  predictAQI(): void {
    this.error = '';

    if (this.pm25 === null || this.co === null || this.no2 === null) {
      this.error = 'Please fill in all pollutant values.';
      return;
    }

    this.loading = true;

    this.aqiService.predict({
      city: this.city,
      pm25: this.pm25,
      co: this.co,
      no2: this.no2
    }).subscribe({
      next: (response: PredictResponse) => {
        this.aqi = response.aqi;
        this.label = response.category;
        this.advice = response.advice;
        this.loading = false;
      },
      error: (err) => {
        console.error('Prediction failed', err);
        this.error = err?.error?.error || 'Prediction failed. Please try again.';
        this.loading = false;
      }
    });
  }

  getRingClass(): string {
    const category = this.label.toLowerCase();

    if (category.includes('good')) return 'low';
    if (category.includes('moderate')) return 'medium';
    return 'high';
  }
}