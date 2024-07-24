import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth/auth.service';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@Component({
  selector: 'app-semester-grades',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, CommonModule],
  templateUrl: './semester-grades.component.html',
  styleUrls: ['./semester-grades.component.css'],
  providers: [AuthService],
})
export class SemesterGradesComponent implements OnInit {
  grades: any[] = [];
  courseGrades = {
    name: '',
    e1_percentage: 0,
    e1_grades: 0,
    p1_percentage: 0,
    p1_grades: 0,
    e2_percentage: 0,
    e2_grades: 0,
    p2_percentage: 0,
    p2_grades: 0,
    e3_percentage: 0,
    e3_grades: 0,
    p3_percentage: 0,
    p3_grades: 0,
    percentage_acum: 0.0,
    score_acum: 0.0,
  }

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    //this.loadGrades();
  }

  loadGrades(): void {
    const apiUrl = 'http://127.0.0.1:8000/api/grades/'; // Actualiza con la URL correcta de tu API
    this.http.get(apiUrl).subscribe((data: any) => {
      this.grades = data;
    });
  }
  averageGrades(){
    const courseGrades = this.courseGrades;
    var acumPercentage = 0;
    acumPercentage += this.prom(courseGrades.e1_percentage, courseGrades.e1_grades);
    console.log(courseGrades.e1_grades);
    console.log(courseGrades.e1_percentage);
    acumPercentage += this.prom(courseGrades.p1_percentage, courseGrades.p1_grades);
    acumPercentage += this.prom(courseGrades.e2_percentage, courseGrades.e2_grades);
    acumPercentage += this.prom(courseGrades.p2_percentage, courseGrades.p2_grades);
    acumPercentage += this.prom(courseGrades.e3_percentage, courseGrades.e3_grades);
    acumPercentage += this.prom(courseGrades.p3_percentage, courseGrades.p3_grades);
    this.courseGrades.percentage_acum = acumPercentage;
    console.log(acumPercentage);
  }
  prom(percentage: number, grades: number){
    return percentage * grades / 20;
  }
}