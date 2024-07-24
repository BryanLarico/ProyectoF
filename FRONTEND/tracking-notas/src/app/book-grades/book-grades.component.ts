import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-book-grades',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './book-grades.component.html',
  styleUrls: ['./book-grades.component.css'],
  providers: [AuthService],
})
export class BookGradesComponent implements OnInit {
  courses: any[] = [];
  overallAverage: number = 0; 

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadCourses();
  }

  loadCourses(): void {
    const apiUrl = 'http://127.0.0.1:8000/api/courses/'; // Actualiza con la URL correcta de tu API
    this.http.get(apiUrl).subscribe((data: any) => {
      this.courses = data;
      this.calculateOverallAverage();
    });
  }

  calculateOverallAverage(): void {
    const totalCredits = this.courses.reduce((sum, course) => sum + course.credits, 0);
    const totalGradePoints = this.courses.reduce((sum, course) => sum + (course.grade * course.credits), 0);
    this.overallAverage = totalGradePoints / totalCredits;
  }
}