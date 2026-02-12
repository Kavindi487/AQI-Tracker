import { Component } from '@angular/core';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule, NavbarComponent],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  city = 'Colombo';
  pm25: number | null = null;
  co: number | null = null;
  no2: number | null = null;

  aqi: number | null = null;
  label = '—';

  predictMock() {
    // temporary demo logic until Flask API is connected
    const pm = this.pm25 ?? 0;
    const c = this.co ?? 0;
    const n = this.no2 ?? 0;
    const bias = this.city === 'Colombo' ? 10 : this.city === 'Kandy' ? 6 : 4;

    const val = Math.min(500, Math.max(0, pm * 0.6 + c * 12 + n * 0.25 + bias));
    this.aqi = Math.round(val);

    this.label =
      this.aqi <= 50 ? 'Good' :
      this.aqi <= 100 ? 'Moderate' :
      this.aqi <= 150 ? 'Unhealthy (Sensitive)' :
      this.aqi <= 200 ? 'Unhealthy' :
      this.aqi <= 300 ? 'Very Unhealthy' : 'Hazardous';
  }
}
