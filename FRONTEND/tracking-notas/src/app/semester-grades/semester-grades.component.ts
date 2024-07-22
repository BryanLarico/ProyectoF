import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-semester-grades',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './semester-grades.component.html',
  styleUrls: ['./semester-grades.component.css'],
  providers: [AuthService],
})
export class SemesterGradesComponent implements OnInit {
  grades: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadGrades();
  }

  loadGrades(): void {
    const apiUrl = 'http://127.0.0.1:8000/api/grades/'; // Actualiza con la URL correcta de tu API
    this.http.get(apiUrl).subscribe((data: any) => {
      this.grades = data;
    });
  }
}