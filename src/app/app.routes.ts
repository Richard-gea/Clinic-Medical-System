import { Routes } from '@angular/router';
import { HomeComponent } from './features/home/home.component';
import { LoginComponent } from './features/auth/login.component';
import { RegisterComponent } from './features/auth/register.component';
import { DoctorsComponent } from './features/doctors/doctors.component';
import { DiseasesComponent } from './features/diseases/diseases.component';
import { AppointmentsComponent } from './features/appointments/appointments.component';
import { AppointmentFormComponent } from './features/appointments/appointment-form.component';
import { UsersComponent } from './features/users/users.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'home', component: HomeComponent, canActivate: [authGuard] },
  { path: 'doctors', component: DoctorsComponent, canActivate: [authGuard] },
  { path: 'diseases', component: DiseasesComponent, canActivate: [authGuard] },
  { path: 'appointments', component: AppointmentsComponent, canActivate: [authGuard] },
  { path: 'appointments/new', component: AppointmentFormComponent, canActivate: [authGuard] },
  { path: 'users', component: UsersComponent, canActivate: [authGuard] },

  { path: '**', redirectTo: '/login' }
];
