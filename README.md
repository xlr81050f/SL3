#  Django Bookstore Project

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
![Screenshot 2025-04-23 150458](https://github.com/user-attachments/assets/e45ea261-c425-4342-8922-b11105377fb8)
![Screenshot 2025-04-23 150452](https://github.com/user-attachments/assets/f82c02d7-03e9-4c9f-beef-0efe1d17cc4a)
![Screenshot 2025-04-23 150445](https://github.com/user-attachments/assets/79bb0089-bef7-4cdf-9fa2-485a213c56ae)
![Screenshot 2025-04-23 150400](https://github.com/user-attachments/assets/8fa23a06-ce66-4440-bce5-49c83ddd0d39)
![Screenshot 2025-04-23 150353](https://github.com/user-attachments/assets/d1511aad-aa7c-4d92-b535-72d2216c29b3)
![Screenshot 2025-04-23 150346](https://github.com/user-attachments/assets/d985d4bc-8f57-431e-bab6-26e7b9637df4)


### 🐳 Docker Notes
Dockerfile: builds the Django we!

![435487874-5cf0214f-7f8e-492c-9e65-6c9f96486d89](https://github.com/user-attachments/assets/d9ceb837-abc2-4857-950c-9dc8a66cfd12)
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
