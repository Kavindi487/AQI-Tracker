import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

interface CityRisk {
  name: string;
  aqi: number;
  risk: 'Low' | 'Medium' | 'High';
  x: number;
  y: number;
  pollutants: {
    pm25: number;
    co: number;
    no2: number;
  };
}

@Component({
  selector: 'app-cities',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './cities.component.html',
  styleUrl: './cities.component.css'
})
export class CitiesComponent {
  selectedCity: CityRisk | null = null;

  cities: CityRisk[] = [
    {
      name: 'Jaffna',
      aqi: 58,
      risk: 'Medium',
      x: 228,
      y: 72,
      pollutants: { pm25: 18.4, co: 0.7, no2: 17.2 }
    },
    {
      name: 'Anuradhapura',
      aqi: 44,
      risk: 'Low',
      x: 192,
      y: 152,
      pollutants: { pm25: 12.5, co: 0.5, no2: 12.8 }
    },
    {
      name: 'Trincomalee',
      aqi: 63,
      risk: 'Medium',
      x: 258,
      y: 165,
      pollutants: { pm25: 20.1, co: 0.8, no2: 18.4 }
    },
    {
      name: 'Kandy',
      aqi: 49,
      risk: 'Low',
      x: 190,
      y: 245,
      pollutants: { pm25: 14.0, co: 0.6, no2: 15.0 }
    },
    {
      name: 'Colombo',
      aqi: 92,
      risk: 'Medium',
      x: 116,
      y: 292,
      pollutants: { pm25: 29.6, co: 1.0, no2: 24.1 }
    },
    {
      name: 'Galle',
      aqi: 134,
      risk: 'High',
      x: 142,
      y: 394,
      pollutants: { pm25: 41.8, co: 1.4, no2: 31.3 }
    },
    {
      name: 'Batticaloa',
      aqi: 116,
      risk: 'High',
      x: 272,
      y: 282,
      pollutants: { pm25: 35.2, co: 1.2, no2: 28.5 }
    }
  ];

  ngOnInit(): void {
    this.selectedCity = this.cities[0];
  }

  selectCity(city: CityRisk): void {
    this.selectedCity = city;
  }

  getRiskClass(risk: 'Low' | 'Medium' | 'High'): string {
    if (risk === 'Low') return 'low';
    if (risk === 'Medium') return 'medium';
    return 'high';
  }
}