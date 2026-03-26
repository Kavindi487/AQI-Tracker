import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './about.component.html',
  styleUrl: './about.component.css'
})
export class AboutComponent {
  features = [
    {
      title: 'AQI Prediction',
      description: 'Uses machine learning to estimate AQI values based on pollutant metrics such as PM2.5, CO, and NO₂.'
    },
    {
      title: 'City Risk Insights',
      description: 'Shows city-level risk visualization so users can understand where pollution conditions are low, medium, or high.'
    },
    {
      title: 'Health Awareness',
      description: 'Provides easy-to-understand guidance so users can take precautions when air quality becomes unhealthy.'
    }
  ];

  stack = ['Angular', 'Flask', 'Scikit-learn', 'REST API', 'Responsive UI'];
}