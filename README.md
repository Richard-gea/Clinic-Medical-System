# Medical Appointment Management System

A comprehensive full-stack web application for managing medical appointments, doctors, diseases, and user profiles. Built with Angular 18 for the frontend and Django REST Framework for the backend.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Database Models](#database-models)
- [Project Structure](#project-structure)
- [Authentication & Authorization](#authentication--authorization)
- [Development Workflow](#development-workflow)

---

## 🎯 Overview

The Medical Appointment Management System is a modern, scalable solution designed to streamline healthcare appointment scheduling. It enables patients to:
- Browse available doctors and their specialties
- View disease information and prevention methods
- Book and manage appointments
- Track appointment history and status

Administrators can:
- Manage user accounts and roles
- Monitor system activity
- Ensure data integrity through cascade delete operations

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: Angular 18 (Standalone Components)
- **Routing**: Angular Router with Route Guards
- **State Management**: Angular Signals & Computed Properties
- **HTTP Client**: HttpClient with Interceptors
- **Styling**: CSS3 with Responsive Design
- **Build Tool**: Angular CLI

### Backend
- **Framework**: Django 5.2.14
- **API**: Django REST Framework
- **Database**: MongoDB (via django-mongodb-backend)
- **Authentication**: Token-based Authentication
- **ORM**: Django MongoDB ODM
- **CORS**: django-cors-headers

### Database
- **MongoDB** - NoSQL document database
- **Storage**: Media files (doctor images, PDFs, disease images)

---

## ✨ Features

### Authentication & Authorization
- ✅ User Registration with email validation
- ✅ Secure Login with token-based authentication
- ✅ Role-based access control (Patient, Admin)
- ✅ Persistent login state with localStorage
- ✅ Protected routes with Auth Guard

### Patient Features
- 📋 View list of available doctors
- 🏥 Browse disease information and prevention methods
- 📅 Book appointments with doctors
- 📊 Manage personal appointments (view, cancel, reschedule)
- 👤 View and update user profile

### Admin Features
- 👥 Manage user accounts and roles
- 👨‍⚕️ Add, edit, and remove doctors
- 🦠 Add, edit, and remove diseases
- 📈 View system statistics and appointment data
- 🗑️ Hard delete functionality with cascade relations

### Data Management
- ✅ Hard delete with cascade relations
- ✅ Appointment cascade deletion when doctor is removed
- ✅ Real-time validation and error handling
- ✅ Audit trail with timestamps

---

## 🏗️ Project Architecture

### Frontend Architecture (Angular)
```
src/app/
├── core/                    # Core functionality
│   ├── guards/             # Auth Guard
│   ├── interceptors/       # HTTP Logger Interceptor
│   ├── models/             # TypeScript Interfaces
│   └── services/           # API Services
├── features/               # Feature modules
│   ├── auth/              # Login & Register
│   ├── appointments/      # Appointment management
│   ├── doctors/           # Doctor listing
│   ├── diseases/          # Disease information
│   ├── users/             # User management (Admin)
│   └── home/              # Dashboard
├── shared/                # Shared components
│   └── navbar/           # Navigation bar
└── app.routes.ts         # Route configuration
```

### Backend Architecture (Django)
```
backend/
├── apps/
│   ├── accounts/         # User authentication & management
│   ├── appointments/     # Appointment booking & management
│   ├── diseases/         # Disease information
│   └── doctors/          # Doctor profiles
├── config/               # Project settings
│   ├── settings.py      # Django configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI server
└── manage.py            # Django management script
```

---

## 📦 Prerequisites

### System Requirements
- Node.js 18+ or higher
- Python 3.9+
- MongoDB 4.4+ or MongoDB Atlas
- npm or yarn (Node package manager)

### Environment Variables
Create a `.env` file in the `backend` directory:
```env
MONGODB_URI=mongodb://localhost:27017/medical_system
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🚀 Installation & Setup

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB connection**
   - Update `backend/config/settings.py` with your MongoDB URI
   - Default: `mongodb://localhost:27017/medical_system`

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd src
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure API endpoint**
   - Update `src/environments/environment.ts`:
   ```typescript
   export const environment = {
     apiUrl: 'http://localhost:8000/api'
   };
   ```

4. **Build the project** (optional)
   ```bash
   ng build
   ```

---

## ▶️ Running the Application

### Start Backend Server
```bash
cd backend
python manage.py runserver
```
- Backend runs on: `http://127.0.0.1:8000`
- API documentation: `http://127.0.0.1:8000/admin` (for admin panel)

### Start Frontend Development Server
```bash
cd src
ng serve
```
- Frontend runs on: `http://localhost:4200`
- Opens automatically in default browser

### Access the Application
- **Frontend**: http://localhost:4200
- **Backend API**: http://localhost:8000/api
- **Admin Panel**: http://localhost:8000/admin

---

## 📡 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Authentication Endpoints

**POST /auth/register/**
- Register new user
- Request: `{ email, password, full_name }`
- Response: `{ user, token }`

**POST /auth/login/**
- User login
- Request: `{ email, password }`
- Response: `{ user, token }`

### Doctor Endpoints

**GET /doctors/**
- List all doctors
- Query params: `search, disease, ordering`

**POST /doctors/**
- Create new doctor (Admin only)
- Request: `{ full_name, email, phone, profile_image, license_pdf, diseases }`

**GET /doctors/{id}/**
- Get doctor details

**PUT /doctors/{id}/**
- Update doctor (Admin only)

**DELETE /doctors/{id}/**
- Delete doctor (Admin only) - Hard delete with cascade

### Disease Endpoints

**GET /diseases/**
- List all diseases
- Query params: `search, ordering`

**POST /diseases/**
- Create new disease (Admin only)
- Request: `{ name, description, symptoms, prevention, image }`

**GET /diseases/{id}/**
- Get disease details

**PUT /diseases/{id}/**
- Update disease (Admin only)

**DELETE /diseases/{id}/**
- Delete disease (Admin only) - Hard delete with cascade

### Appointment Endpoints

**GET /appointments/**
- List user appointments
- Query params: `status`
- Statuses: `pending, confirmed, cancelled, completed`

**POST /appointments/**
- Create new appointment
- Request: `{ patient, doctor, appointment_date, appointment_time, notes }`

**GET /appointments/{id}/**
- Get appointment details

**PUT /appointments/{id}/**
- Update appointment
- Request: `{ status, notes }`

**DELETE /appointments/{id}/**
- Delete appointment - Hard delete

### User Endpoints

**GET /users/**
- List all users (Admin only)

**GET /users/{id}/**
- Get user profile

**PUT /users/{id}/**
- Update user profile

---

## 🗄️ Database Models

### User Model
```python
{
  id: ObjectId,
  email: String (unique),
  password: String (hashed),
  full_name: String,
  role: String (patient, admin),
  created_at: DateTime,
  updated_at: DateTime
}
```

### Doctor Model
```python
{
  id: ObjectId,
  full_name: String,
  email: String (unique),
  phone: String,
  profile_image: File,
  license_pdf: File,
  diseases: [Disease] (ManyToMany),
  is_deleted: Boolean (soft delete field),
  created_at: DateTime,
  updated_at: DateTime
}
```

### Disease Model
```python
{
  id: ObjectId,
  name: String (unique),
  description: String,
  symptoms: String,
  prevention: String,
  image: File,
  is_deleted: Boolean (soft delete field),
  created_at: DateTime,
  updated_at: DateTime
}
```

### Appointment Model
```python
{
  id: ObjectId,
  patient: User (ForeignKey),
  doctor: Doctor (ForeignKey),
  appointment_date: Date,
  appointment_time: Time,
  notes: String,
  status: String (pending, confirmed, cancelled, completed),
  created_at: DateTime,
  updated_at: DateTime
}
```

---

## 📁 Project Structure

```
B29_Angular_Django/
├── src/                           # Angular Frontend
│   ├── app/
│   │   ├── core/
│   │   │   ├── guards/
│   │   │   ├── interceptors/
│   │   │   ├── models/
│   │   │   └── services/
│   │   ├── features/
│   │   ├── shared/
│   │   └── app.routes.ts
│   ├── environments/
│   ├── angular.json
│   ├── package.json
│   └── tsconfig.json
│
├── backend/                       # Django Backend
│   ├── apps/
│   │   ├── accounts/
│   │   ├── appointments/
│   │   ├── diseases/
│   │   └── doctors/
│   ├── config/
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md                      # This file
```

---

## 🔐 Authentication & Authorization

### Token-Based Authentication
- Users receive a token upon successful login
- Token stored in localStorage
- Attached to all API requests via HTTP header
- Auth Guard protects routes from unauthorized access

### Role-Based Access Control
- **Patient**: Can view doctors/diseases, book appointments
- **Admin**: Full access to all resources and management features

### Protected Routes
- `/login` - Public
- `/register` - Public
- `/home` - Protected (authenticated users)
- `/doctors` - Protected (authenticated users)
- `/diseases` - Protected (authenticated users)
- `/appointments` - Protected (authenticated users)
- `/users` - Protected (admin only)

---

## 💻 Development Workflow

### Adding a New Feature

1. **Create components/services** in the appropriate feature folder
2. **Add routes** to `app.routes.ts`
3. **Create API endpoints** in Django backend
4. **Add services** to call backend APIs
5. **Implement guards** if access restrictions needed
6. **Test locally** before deployment

### Code Standards

**Frontend (Angular)**
- Use standalone components
- Implement TypeScript strict mode
- Use Angular Signals for state management
- Follow Angular style guide

**Backend (Django)**
- Follow PEP 8 style guide
- Use Django best practices
- Implement proper error handling
- Use Django's ORM for database queries

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/feature-name

# Commit changes
git add .
git commit -m "Description of changes"

# Push to repository
git push origin feature/feature-name

# Create pull request
```

---

## 🐛 Troubleshooting

### MongoDB Connection Issues
```
Error: No module named 'django_mongodb_backend'
Solution: pip install django-mongodb-backend pymongo
```

### CORS Errors
```
Error: Access to XMLHttpRequest blocked
Solution: Ensure django-cors-headers is installed and configured in settings.py
```

### Port Already in Use
```bash
# Find process using port 8000 (backend)
netstat -ano | findstr :8000

# Find process using port 4200 (frontend)
netstat -ano | findstr :4200

# Kill process
taskkill /PID <PID> /F
```

### Module Not Found (Angular)
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

---

## 📚 Additional Resources

- [Angular Documentation](https://angular.io/docs)
- [Django Documentation](https://docs.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org)
- [MongoDB Documentation](https://docs.mongodb.com)
- [TypeScript Handbook](https://www.typescriptlang.org/docs)

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👥 Contributing

Contributions are welcome! Please follow the development workflow outlined above and submit pull requests for review.

---

## 📞 Support

For issues, questions, or suggestions, please create an issue in the repository or contact the development team.

---

**Last Updated**: May 22, 2026  
**Version**: 1.0.0  
**Status**: Production Ready
