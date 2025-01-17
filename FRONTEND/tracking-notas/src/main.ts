import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter, RouterOutlet } from '@angular/router';
import { AppComponent } from './app/app.component';
import { LoginComponent } from './app/auth/login/login.component';
import { SignupComponent } from './app/auth/signup/signup.component';
import { SemesterGradesComponent } from './app/semester-grades/semester-grades.component';
import { BookGradesComponent } from './app/book-grades/book-grades.component';
import { provideHttpClient } from '@angular/common/http';

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    provideRouter([
      { path: 'login', component: LoginComponent },
      { path: 'signup', component: SignupComponent },
      { path: 'semester-grades', component: SemesterGradesComponent },
      { path: 'book-grades', component: BookGradesComponent },
      { path: '', redirectTo: '/login', pathMatch: 'full' },
      { path: '**', redirectTo: '' }
    ])
  ]
});