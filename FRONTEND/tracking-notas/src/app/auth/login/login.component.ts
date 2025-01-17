import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [AuthService],
})
export class LoginComponent implements OnInit{
  input = {
    username: '',
    password: '',
  }  

  constructor(private authService: AuthService, private router: Router){

  }

  ngOnInit(): void {
  }
  loginUser(){
    this.authService.login(this.input).subscribe(
      response => {
        console.log(response) //Borrar despues
        //alert('User ' + this.input.username + ' logged.');
        this.router.navigate(['../../semester-grades']);
      },
      error => console.log('Error: ', error)
    )
    console.log(this.input);
  }
}