# Census Automation System

## 🧾 Project Overview
Census Automation System is a **Django-based** web application developed to automate and digitize the population census process in Bangladesh. It streamlines the data collection and verification workflow, improving accuracy, accessibility, and administrative control. Inspired by the 2022 digital census initiative, this project serves as a scalable, secure, and intelligent solution for future national population data drives.

---

## 🔑 Key Features

- 🔐 **Secure Authentication** – Role-based login system for enumerators and admins
- 📄 **Dynamic Census Forms** – Validated and categorized user input fields
- 📊 **Admin Dashboard** – Real-time review, edit, approval, and rejection of submissions
- ♻️ **Record Update Mechanism** – Users can edit previously submitted data
- 📁 **Data Export & Reports** – Filter and download structured datasets
- 🤖 **Face Recognition (Planned)** – Enumerator identity verification
- 🗺️ **GIS Mapping (Planned)** – Visualize data by location

---

## 🛠️ Technology Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Backend:** Django (Python)
- **Database:** SQLite (for development), PostgreSQL (for deployment)
- **Server:** Gunicorn
- **Deployment:** [Render](https://render.com)

---

## 🏗️ System Architecture

Three-layered architecture:
1. **Presentation Layer** – User interfaces (Forms, Dashboards)
2. **Logic Layer** – Django views and form validation
3. **Data Layer** – Persistent storage using SQLite/PostgreSQL

---

## 🔄 Workflow Overview

1. User registers/logs in
2. Submits census form
3. Admin receives data for review
4. Admin can accept, reject, or request an update
5. User edits if necessary
6. Data is finalized and stored

---

## 🚀 Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/takitamim/Census_Automation_System.git
cd Census_Automation_System
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

Access your app at: [http://localhost:8000](http://localhost:8000)

---

## 🌐 Deployment on Render (Free Hosting)

### Requirements:
- A free [Render](https://render.com) account
- PostgreSQL instance created in Render dashboard

### Deployment Steps:
1. Push code to GitHub
2. Connect the repo to Render Web Service
3. Add environment variables:
   - `DATABASE_URL` (from Render PostgreSQL)
   - `SECRET_KEY` (use Django secret key generator)
4. Set build & start commands:
   ```bash
   # Build Command
   pip install -r requirements.txt

   # Start Command
   gunicorn Census_Automation_System.asgi:application -k uvicorn.workers.UvicornWorker
   ```
5. Create superuser via Render shell:
   ```bash
   python manage.py createsuperuser
   ```

---

## 🧪 Running Tests
To run unit tests for views, forms, and models:
```bash
python manage.py test
```

Tests ensure:
- Census form validation
- Admin approval workflows
- View routing and permissions

---

## 👥 Demo Credentials

You can use the following test user to explore the application:

- **Username:** `testuser`
- **Password:** `testpass`

---

## 🌱 Future Scope

- ✅ Mobile App (PWA/Flutter)
- ✅ Biometric (Face) Verification
- ✅ GIS-based Data Visualization
- ✅ National ID Integration
- ✅ Multilingual UI
---

## 🧩 Contributing

### How to Contribute:
1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push and create a Pull Request:
   ```bash
   git push origin feature/YourFeatureName
   ```

---

## 📦 Push Remaining Files to GitHub

```bash
git add .
git commit -m "Add remaining project files"
git push origin master
```


**Developed by:** Taki Tamim  
**Institution:** RUET, Department of CSE  
**Project Type:** Academic Web Development Project