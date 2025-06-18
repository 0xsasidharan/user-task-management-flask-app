
# 👤📝 Flask User & Task REST API

A simple and extendable RESTful API for managing users and their associated tasks — built with **Python Flask**.
This project follows a clean backend architecture using **Flask-Smorest**, with validation, modular blueprints, and OpenAPI docs.

---

## 📝 Features

* Full CRUD for Users
* Full CRUD for Tasks
* Each user includes:

  * `name` (required)
  * `user_id` (UUID)
* Each task includes:

  * `title` (required)
  * `user_id` (must exist)
  * `task_id` (UUID)
* Input validation using Marshmallow
* RESTful structure using Blueprints and MethodView
* OpenAPI documentation via Flask-Smorest

---

## 🚧 Project Progress Checklist

| Day | Feature                                | Status    |
| --- | -------------------------------------- | --------- |
| 1   | Basic Flask App with GET, POST, DELETE | ✅ Done    |
| 2   | Add PUT for updating tasks             | ✅ Done    |
| 3   | Add input validation via Marshmallow   | ✅ Done    |
| 4   | Refactor with Blueprints               | ✅ Done    |
| 5   | Use MethodView Class-Based Views       | ✅ Done    |
| 6   | Add Flask-Smorest with Swagger UI      | ✅ Done    |
| 7   | Add Docker Containerization            | ✅ Done |
| 8   | Database Integration with SQLAlchemy   | ✅ Done |
| 9   | Add JWT Authentication                 | ⬜ Pending |

---

## 📘 API Endpoints

### 🔹 `GET /users`

**Description:** Retrieve all users.

**Responses:**

* `200 OK`: Returns a list of users.

---

### 🔹 `POST /users`

**Description:** Create a new user.

**Request Body (JSON):**

```json
{
  "name": "John Doe"
}
```

**Responses:**

* `201 Created`: Returns the created user.

---

### 🔹 `GET /users/<user_id>`

**Description:** Retrieve a single user by ID.

**Responses:**

* `200 OK`: Returns the user.
* `404 Not Found`: If the user doesn't exist.

---

### 🔹 `DELETE /users/<user_id>`

**Description:** Delete a user by ID.

**Responses:**

* `200 OK`: Confirmation message.
* `404 Not Found`: If the user doesn't exist.

---

### 🔸 `GET /tasks`

**Description:** Retrieve all tasks.

**Responses:**

* `200 OK`: Returns a list of tasks.

---

### 🔸 `POST /tasks`

**Description:** Create a new task linked to a user.

**Request Body (JSON):**

```json
{
  "title": "Finish reading",
  "user_id": "your_user_id_here"
}
```

**Responses:**

* `201 Created`: Returns the created task.
* `404 Not Found`: If the `user_id` is invalid.

---

### 🔸 `GET /tasks/<task_id>`

**Description:** Retrieve a task by ID.

**Responses:**

* `200 OK`: Returns the task.
* `404 Not Found`: If the task doesn't exist.

---

### 🔸 `PUT /tasks/<task_id>`

**Description:** Update an existing task.

**Request Body (JSON):**

```json
{
  "title": "Finish writing notes"
}
```

**Responses:**

* `200 OK`: Returns the updated task.
* `404 Not Found`: If the task doesn't exist.

---

### 🔸 `DELETE /tasks/<task_id>`

**Description:** Delete a task by ID.

**Responses:**

* `200 OK`: Confirmation message.
* `404 Not Found`: If the task doesn't exist.

---

# 🔧 Local Installation

## 📦 Using Python (venv)

### Create virtual environment & activate

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Linux/macOS
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
flask run
```

---

## 🐳 Using Docker

### Build Docker image

```bash
docker build -t flask-user-task-api .
```

### Run container

```bash
docker run -p 5000:5000 flask-user-task-api
```

### Run using docker-compose

```bash
docker-compose up --build
```

---
