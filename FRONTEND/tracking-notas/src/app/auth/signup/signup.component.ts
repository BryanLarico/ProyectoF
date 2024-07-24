import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, CommonModule],
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
  providers: [AuthService],
})
export class SignupComponent implements OnInit{
  register = {
    username: '',
    password: '',
    email: '',
    is_staff: true,
  }  

  constructor(private authService: AuthService){
  }

  ngOnInit(): void {
  }
  registerUser(){
    this.authService.signup(this.register).subscribe(
      response => {
        alert('User ' + this.register.username + ' created')
      },
      error => console.log('Error:', error)
    )
    console.log(this.register);
  }
}