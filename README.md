# 🚀 Task Manager API

*A Production-Ready Backend Project with Flask, Docker & CI/CD*

---

## 📌 Overview

This project is a **RESTful Task Management API** built using **Flask**, designed with real-world backend practices including **testing, containerization, and CI/CD automation**.

It demonstrates how a backend service is developed, tested, packaged, and deployed using modern DevOps workflows.

---

## ✨ Key Highlights

* 🔹 REST API with full CRUD operations
* 🔹 Input validation & error handling
* 🔹 Unit + Integration testing using pytest
* 🔹 Test coverage reporting
* 🔹 Dockerized application
* 🔹 CI/CD pipeline using GitHub Actions
* 🔹 Automatic Docker image build & push

---

## 🛠️ Tech Stack

| Layer      | Technology         |
| ---------- | ------------------ |
| Backend    | Flask (Python)     |
| Testing    | Pytest, Pytest-Cov |
| Container  | Docker             |
| CI/CD      | GitHub Actions     |
| Versioning | Git & GitHub       |

---

## 📂 Project Structure

```
.
├── app.py
├── utils.py
├── tests/
│   ├── test_utils.py
│   └── test_app.py
├── requirements.txt
├── Dockerfile
└── .github/workflows/ci.yml
```

---

## ⚙️ Running the Application

### 🔹 Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/Task-Manager-Fullstack-Workshop.git
cd Task-Manager-Fullstack-Workshop
pip install -r requirements.txt
python app.py
```

👉 Access at:

```
http://127.0.0.1:5000
```

---

## 🧪 Testing & Coverage

Run tests:

```bash
pytest -v
```

Run with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t task-manager .
```

### Run Container

```bash
docker run -p 5000:5000 task-manager
```

---

## 🌐 Run from Docker Hub

```bash
docker run -p 5000:5000 nkg01/task-manager:latest
```

---

## 🔄 CI/CD Pipeline

This project includes a fully automated CI/CD pipeline using GitHub Actions.

### ✔ On every push:

1. Install dependencies
2. Run tests
3. Generate coverage
4. Build Docker image
5. Push image to Docker Hub

Workflow file:

```
.github/workflows/ci.yml
```

---

## 📡 API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| GET    | /tasks      | Get all tasks  |
| POST   | /tasks      | Create a task  |
| GET    | /tasks/<id> | Get task by ID |
| PUT    | /tasks/<id> | Update task    |
| DELETE | /tasks/<id> | Delete task    |

---

## 🧠 Concepts Demonstrated

* REST API design
* Modular backend architecture
* Unit & integration testing
* Docker containerization
* CI/CD automation
* Secure secrets handling

---

## 🚀 Future Enhancements

* Database integration (PostgreSQL / MongoDB)
* Authentication (JWT)
* Pagination & filtering
* Cloud deployment

---

## 👨‍💻 Author

**Nitesh**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
