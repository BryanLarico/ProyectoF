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
  studentId: number = 1 // Cambiar esto por el ID del estudiante
  courses: any[] = [];
  courseGrades = {
    idUnitReport: 0,
    idCourse: 1,
    idStudent: 1,
    eval_cont1: 0,
    parcial1: 0,
    eval_cont2: 0,
    parcial2: 0,
    eval_cont3: 0,
    parcial3: 0,
  }
  acumFila: number[] = [];
  acumFilaPunt: number[] = [];

  constructor(private authService: AuthService, private http: HttpClient){
  }
  ngOnInit(): void {
    this.loadCourse();
  }

  loadCourse(): void {
    const apiUrl = 'http://127.0.0.1:8000/api/courses/';
    this.http.get(apiUrl).subscribe((data: any) => {
      this.courses = data;
    });
  }

  sendGradesHTML(){
    this.authService.sendGrades(this.courseGrades).subscribe(
      response => {
        console.log(this.courseGrades);
      },
      error => console.log('Error:', error)
    )
  }
  loadGrades(idCourse: number): void {
    const apiGradesUrl = `http://127.0.0.1:8000/api/unitreports/student/${this.studentId}/`;
    this.http.get<any []>(apiGradesUrl).subscribe((data) => {
      data.forEach((unitReport: any) => {
        if (!this.courseGrades[unitReport.idCourse]) {
          this.courseGrades[unitReport.idCourse] = unitReport;
        }
      });
    }, error => {
      console.log('Error loading grades:', error);
    });
  }


  averageGrades(){
    let acumPercentage = 0;
    for(let course of this.courses){
      const courseGrades = this.courseGrades;
      acumPercentage += this.prom(courseGrades.eval_cont1, course.e1);
      console.log(courseGrades.eval_cont1);
      acumPercentage += this.prom(courseGrades.parcial1, course.p1);
      acumPercentage += this.prom(courseGrades.eval_cont2, course.e2);
      acumPercentage += this.prom(courseGrades.parcial2, course.p2);
      acumPercentage += this.prom(courseGrades.eval_cont3, course.e3);
      acumPercentage += this.prom(courseGrades.parcial3, course.p3);
      console.log(acumPercentage);
      this.acumFila.push(acumPercentage);
    }
    this.averageGradesPunt();
  }

  prom(percentage: number, grades: number){
    return percentage * grades / 20;
  }

  averageGradesPunt(){
    let acumPunt = 0;
    for(let acum of this.acumFila){
      acumPunt += acum / 5;
      this.acumFilaPunt.push(acumPunt);

    }
  }
}