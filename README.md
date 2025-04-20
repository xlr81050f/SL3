# 📚 Django Bookstore Project

A full-stack Django application like Amazon but only for books, specifically for managing and ordering books. It includes full user authentication, a session-based cart, custom admin panel, and DevOps integration with Docker and Jenkins.

---

## 🚀 Project Overview

This project allows users to:

- Browse all books without logging in
- View detailed information about each book
- Register/Login to add books to the cart
- View and confirm orders
- Track order history
- Admin users can manage books and orders via a custom admin panel (no Django Admin used)

All functionalities are built using **Class-Based Views (CBVs)** and **manual HTML forms** — no Django forms or function-based views (FBVs).

---

## ⚙️ Setup & Run Instructions

### ✅ Prerequisites
- Docker Desktop installed
- Git installed

### 📦 Clone the Project

```bash
git clone <your-repo-url>
cd bookstore_project
🐳 Run with Docker Compose
- docker compose up --build
The app will be available at: http://localhost:8000

🧑‍💻 Create Admin User
- docker compose exec web python manage.py shell < init_admin.py
``` 
### 🧰 Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS (Bootstrap)

Database: SQLite (can be swapped with PostgreSQL)

DevOps: Docker, Docker Compose, Jenkins

### 📸 Screenshots
1. ![WhatsApp Image 2025-04-20 at 23 18 21_f4b2e8cd](https://github.com/user-attachments/assets/00624b98-1e96-4642-8212-2032843c79b2)
2. ![WhatsApp Image 2025-04-20 at 23 20 54_f92c6916](https://github.com/user-attachments/assets/7558be2c-8781-4ca2-93d7-36e780e85ed8)
3. ![WhatsApp Image 2025-04-20 at 23 21 02_82068fa9](https://github.com/user-attachments/assets/cb150eed-2468-4d22-9f6a-6aa443befe64)

### 🐳 Docker Notes
Dockerfile: builds the Django web app

docker-compose.yml: defines the web service and database

Uses volume mounts for live code reloads

Accessible at: http://localhost:8000

### 🔁 Jenkins CI/CD
Jenkinsfile is included for CI/CD:

Runs tests

Builds Docker image

Deploys the container

You can connect Jenkins to your GitHub repo and set up automatic builds on push.

### 📂 Folder Structure
```
bookstore_project/
├── books/
├── accounts/
├── cart/
├── orders/
├── admin_panel/
├── templates/
├── static/
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── init_admin.py
└── manage.py
```
### 📜 License
This project is for educational use only.
