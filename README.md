# 🏫 CampusPro: College Management System

An advanced, responsive **College Management System** built with Python, Django, and Bootstrap. CampusPro is designed to streamline administrative workflows, simplify student-staff communication, and provide intuitive dashboards for all user roles.

---

## 🚀 Quick Start Guide

To get CampusPro up and running locally, follow these steps.

### 📋 Prerequisites
Ensure you have **Python 3.x** installed. You can check your version using:
```bash
python --version
```

### 🛠️ Local Environment Setup

1. **Clone the Repository & Navigate to the Project:**
   ```bash
   git clone https://github.com/Saikrishna1124/CampusPro.git
   cd CampusPro
   ```

2. **Activate the Virtual Environment:**
   Depending on your terminal/operating system, execute the appropriate command:
   * **Git Bash (Windows/Linux/macOS):**
     ```bash
     source .venv/Scripts/activate
     ```
   * **PowerShell:**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   * **Command Prompt (CMD):**
     ```cmd
     .\.venv\Scripts\activate.bat
     ```

3. **Install Dependencies:**
   With the virtual environment active, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations:**
   Ensure the database is up-to-date:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server:**
   * **Using activated shell:**
     ```bash
     python manage.py runserver
     ```
   * **Direct execution (Git Bash - without activating):**
     ```bash
     ./.venv/Scripts/python.exe manage.py runserver
     ```
   * **Direct execution (PowerShell/CMD - without activating):**
     ```powershell
     .\.venv\Scripts\python.exe manage.py runserver
     ```

6. **Access the Application:**
   Open your browser and navigate to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 👥 Roles & Feature Set

### 🔑 A. Administrator (HOD)
* **Overall Metrics & Performance**: View interactive charts summarizing student and staff numbers, course distributions, and attendance metrics.
* **Staff & Student Management**: Full CRUD operations (Add, View, Update, Delete) on student and staff profiles.
* **Academic Planning**: Add and manage Courses, Subjects, and Session Years.
* **Leave Management**: Approve or reject leave applications submitted by students and staff.
* **Feedback Systems**: Read and reply directly to feedback submitted by student and staff users.

### 📝 B. Staff / Faculty
* **Dashboard Summary**: Visual analytics showcasing attendance rates of assigned courses, class averages, and leave history.
* **Attendance System**: Take, review, and update student attendance for assigned subjects.
* **Grades & Results**: Log and edit final exam and assignment marks for students.
* **Leave Requests**: Apply for professional leaves directly from the portal.
* **Direct Feedback**: Send feedback messages and feature requests directly to the HOD.

### 🎓 C. Student
* **Academic Analytics**: Visually track personal attendance rates, performance stats, and subject progression.
* **Grades Portal**: View exam results and assignment grades securely.
* **Attendance Log**: Access complete history of daily attendance across all registered courses.
* **Leave Applications**: Apply for leave requests and track approval statuses in real-time.
* **HOD Helpline**: Send direct feedback and receive replies from administrators.

---

## 🛠️ Technology Stack

* **Backend Framework**: [Django (Python)](https://www.djangoproject.com/)
* **Database**: SQLite (default local development)
* **Styling & Layout**: Bootstrap 4 / 5, Custom CSS
* **Frontend Scripting**: JavaScript, jQuery, AJAX
* **Deployment Integration**: Ready for Vercel and PythonAnywhere

---

## 📁 Project Architecture

```
CampusPro/
│
├── api/
│   └── index.py                 # Serverless WSGI entry point for Vercel
│
├── student_management_project/  # Project Configuration
│   ├── settings.py              # Settings, Auth Backends, and Middleware
│   ├── urls.py                  # Root URLs routing
│   └── wsgi.py                  # WSGI config
│
├── student_management_app/      # Main Application Folder
│   ├── templates/               # HTML Templates (Base, Login, Registrations, HOD/Staff/Student panels)
│   ├── static/                  # CSS, JS, and Admin Panel Assets
│   ├── models.py                # CustomUser & Profile database models
│   ├── views.py                 # Sign-in, Sign-up, and generic views
│   ├── HodViews.py              # Views & actions specific to HOD
│   ├── StaffViews.py            # Views & actions specific to Staff
│   ├── StudentViews.py          # Views & actions specific to Students
│   └── EmailBackEnd.py          # Custom backend for authentication using Email
│
├── vercel.json                  # Vercel deployment configurations
├── requirements.txt             # Python packages
└── manage.py                    # Django administration tool
```

---

## 🔒 Security & Password Upgrades

This project utilizes a customized **Email-based authentication backend** (`EmailBackEnd.py`).
1. **Password Hashing**: New accounts registered through the sign-up page are hashed using Django's default PBKDF2 secure hashing algorithm.
2. **Seamless Upgrade**: Legacy users stored with plain-text passwords will automatically have their passwords securely hashed on their next successful login.
