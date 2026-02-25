# Student Management System (Django + DevOps)

A full-stack **Student Management System** built using **Django** and **PostgreSQL**, containerized with **Docker** and orchestrated using **Docker Compose** and **Kubernetes**. Designed to manage students, marks, attendance, analytics, and role-based access (Admin & Student).

This project follows **real-world academic ERP logic** and is suitable for **college portals** and **learning management systems**.

---

## 🎯 Project Highlights

- **Full-stack web application** with Django backend and Bootstrap frontend
- **Role-based authentication** - separate dashboards for staff and students
- **Containerized deployment** - Docker + Docker Compose + Kubernetes ready
- **CI/CD pipeline** - GitHub Actions for automated testing and deployment
- **Production-ready** - PostgreSQL database, environment configuration, Gunicorn WSGI server
- **Data export** - CSV and multi-sheet Excel reports

---

## 🚀 Features

### 👨‍💼 Admin / Staff Features
- ✅ Complete CRUD operations for students
- ✅ Upload and manage student images
- ✅ Add subjects and manage marks
- ✅ Daily attendance tracking (editable only for current date)
- ✅ View attendance history for any date
- ✅ **Analytics Dashboard:**
  - Total students count
  - Pass/Fail statistics
  - Department-wise breakdown
  - Average marks percentage
  - Average attendance percentage
  - Low attendance alerts (<75%)
- ✅ **Export Options:**
  - Individual student details (CSV)
  - Individual student marks (CSV)
  - All students + marks (Excel – multi-sheet)
- ✅ Search and pagination for large datasets

---

### 👨‍🎓 Student Features
- ✅ Secure login with role-based access
- ✅ Personal dashboard showing:
  - Profile information
  - Complete marksheet
  - Attendance history
  - Monthly attendance report
- ✅ Dynamic attendance percentage calculation
- ✅ Monthly attendance summary (present/absent/percentage)
- ✅ Read-only access (students cannot modify data)
- ✅ Object-level security (cannot view other students' data)

---

## 🔐 Authentication & Authorization
- Django's built-in authentication system
- Role-based access control:
  - **Staff** → Full administrative access
  - **Student** → Restricted to own data only
- Object-level permissions
- Secure password hashing
- Protected views with decorators
- Safe login/logout with proper redirects

---

## 📊 Attendance System
- Daily attendance marking (Present/Absent)
- ✅ Can mark & edit attendance for **today only**
- ❌ Cannot edit past attendance (data integrity)
- Dynamic percentage calculation
- Monthly attendance reports per student
- Low attendance alerts for administrators

---

## 🛠️ Tech Stack

### Backend
- **Django 4.x** - Web framework
- **Python 3.x** - Programming language
- **PostgreSQL** - Production database
- **Gunicorn** - WSGI HTTP server

### Frontend
- **HTML5** - Markup
- **Bootstrap 5** - UI framework
- **JavaScript** - Client-side interactions

### DevOps & Deployment
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration (k8s manifests included)
- **GitHub Actions** - CI/CD pipeline
- **Nginx** (recommended for production)

### Libraries
- **openpyxl** - Excel file generation
- **Pillow** - Image processing
- **python-decouple** - Environment configuration

---

## 📁 Project Structure

```
Student_Management_System/
├── app/                      # Django application
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Django forms
│   ├── urls.py              # URL routing
│   ├── templates/           # HTML templates
│   └── static/              # CSS, JS, images
├── docker/                   # Docker configuration
│   ├── Dockerfile           # Application container
│   └── docker-compose.yml   # Multi-service setup
├── k8s/                      # Kubernetes manifests
│   ├── deployment.yaml      # App deployment
│   └── postgres.yaml        # Database deployment
├── .github/                  # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── media/                    # User-uploaded files
├── static/                   # Static files
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
├── manage.py                # Django management
└── Readme.md                # Documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL 13+
- Docker & Docker Compose (for containerized deployment)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srivenkatesh03/Student_Management_System.git
   cd Student_Management_System
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```
   Visit http://localhost:8000

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access the application
open http://localhost:8000
```

### Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/

# Check deployment status
kubectl get pods
kubectl get services
```

---

## 🧠 Key Technical Concepts Demonstrated

- ✅ **Django ORM** - Complex model relationships
- ✅ **Business Logic in Models** - Reusable methods
- ✅ **Role-Based Access Control** - Staff vs Student permissions
- ✅ **File Handling** - Image uploads with validation
- ✅ **Data Export** - CSV and Excel generation
- ✅ **Pagination** - Handling large datasets efficiently
- ✅ **Search Functionality** - Dynamic filtering
- ✅ **Authentication** - Secure login/logout
- ✅ **Containerization** - Docker best practices
- ✅ **CI/CD** - Automated testing and deployment
- ✅ **Environment Configuration** - 12-factor app principles

---

## 📸 Screenshots

##Screenshot
<img width="1920" height="1080" alt="student attadance monthly" src="https://github.com/user-attachments/assets/71b2d79b-71c6-409a-892b-aecec20da1c9" />
<img width="1920" height="1080" alt="attadance" src="https://github.com/user-attachments/assets/87868acc-bb8d-45cb-96b8-3b9e3e9f3477" />
<img width="1920" height="1080" alt="view attadance" src="https://github.com/user-attachments/assets/34422ee9-cd4d-47b9-bb02-4bb4ffdccb35" />
<img width="1920" height="1080" alt="add marks" src="https://github.com/user-attachments/assets/08111fb7-0a64-4be2-8c46-5e90ac478bc7" />
<img width="1920" height="1080" alt="mark list" src="https://github.com/user-attachments/assets/712fc15e-f4d4-4b7f-b7c1-ee938adc2493" />
<img width="1920" height="1080" alt="student login mark" src="https://github.com/user-attachments/assets/393b5891-e19d-40d7-bac5-8b28ed155994" />
<img width="1920" height="1080" alt="student attadance" src="https://github.com/user-attachments/assets/86f160de-ca8a-4b2f-a3d2-5ee76883973c" />
<img width="1920" height="1080" alt="student attadance monthly" src="https://github.com/user-attachments/assets/57fbc022-20b7-4500-b1ec-ed64da549b39" />
<img width="1920" height="1080" alt="loginpage" src="https://github.com/user-attachments/assets/f334d702-75e6-49ab-825b-eb87b3cdf1ab" />
<img width="1920" height="1080" alt="dashboard" src="https://github.com/user-attachments/assets/59d6b63b-f105-4edc-bc35-6fa30fa1ae9f" />
<img width="1920" height="1080" alt="student_list" src="https://github.com/user-attachments/assets/91f97cfa-7da7-4253-9f36-e6524808e188" />
<img width="1920" height="1080" alt="student details" src="https://github.com/user-attachments/assets/1b5380cf-f2be-4fb9-b2cb-a58169f3f11f" />
<img width="1920" height="1080" alt="student marks" src="https://github.com/user-attachments/assets/38c1e053-1af6-4dfb-a2c1-672d699b9a0d" />
<img width="1920" height="1080" alt="Screenshot (271)" src="https://github.com/user-attachments/assets/cb615541-9566-49d0-af1d-d231068115d1" />
<img width="1920" height="1080" alt="edit or add" src="https://github.com/user-attachments/assets/a595fbf2-5d55-428b-97df-d014d799bccd" />

---







