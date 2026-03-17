# HRMS Lite — Human Resource Management System

A web-based HRMS application for admins to manage employee records and track daily attendance.

---

## Project Overview

HRMS Lite is a full-stack application that provides a simple, professional HR tool for:
- Managing employee records (add, view, delete)
- Tracking daily attendance (mark, view, filter)
- Dashboard summary with attendance statistics

---

## Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | Python, Django, Django REST Framework |
| Database   | SQLite (dev) / PostgreSQL (prod)    |
| Auth       | None (single admin, no auth required) |
| Deployment | Render (Backend)                    |

---

## API Endpoints

| Method | Endpoint                              | Description                        |
|--------|---------------------------------------|------------------------------------|
| GET    | `/api/employees/`                     | List all employees                 |
| POST   | `/api/employees/`                     | Add a new employee                 |
| DELETE | `/api/employees/<id>/`                | Delete an employee                 |
| GET    | `/api/employees/<id>/attendance/`     | Get attendance for an employee     |
| GET    | `/api/attendance/`                    | List all attendance records        |
| POST   | `/api/attendance/`                    | Mark attendance                    |
| GET    | `/api/attendance/by-employee/`        | Filter attendance by employee      |
| GET    | `/api/attendance/summary/`            | Attendance summary per employee    |

---

## Run Locally

### Prerequisites
- Python 3.10+
- pip

### Steps

```bash
# 1. Clone the repository
git clone <your-github-repo-url>
cd HRMS_backend/HRMS

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Backend will be available at: `http://localhost:8000`

---

## Deployment

- Backend: Deployed on [Render](https://render.com)
- Frontend: Deployed on [Vercel](https://vercel.com) / [Netlify](https://netlify.com)

> Live URLs will be added after deployment.

---

## Assumptions & Limitations

- Single admin user — no authentication or role management
- Leave management, payroll, and advanced HR features are out of scope
- Duplicate attendance for the same employee on the same date is not allowed
- Employee ID and email must be unique across the system
- SQLite is used for local development; switch to PostgreSQL for production

---

## Bonus Features Implemented

- Filter attendance records by date
- Total present days per employee via summary endpoint
- Dashboard summary with employee and attendance counts
