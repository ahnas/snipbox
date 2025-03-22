
![frontend_workingCC](https://github.com/user-attachments/assets/58662da4-8f28-4008-aafc-80075a70ea65)
![api_testingCC](https://github.com/user-attachments/assets/bde8e0a7-bc9c-40f7-8ddb-a83dbe10b750)
# SnipBox Backend API

## Overview
SnipBox is a short note-saving app that lets users save short text snippets and group them with tags. The backend is built using Django Rest Framework (DRF) with JWT authentication.

## Features
- User authentication using JWT (Login, Refresh token)
- CRUD operations for snippets
- Tagging system with unique tag titles
- API documentation using Swagger
- Test cases provided in Postman collection & cURL
- Deployment with Docker (Optional)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository_link>
cd snipbox-backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
# venv\Scripts\activate (For Windows)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database
Modify `settings.py` to set up a PostgreSQL database:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'snipbox_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run database migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

---

## API Documentation

### Authentication APIs
#### 1. Login API
**Endpoint:** `http://127.0.0.1:8000/api/auth/login/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "username": "testuser",
  "password": "testpassword"
}
```
**Response:**
```json
{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>"
}
```

#### 2. Refresh Token API
**Endpoint:** `http://127.0.0.1:8000/api/auth/refresh/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "refresh": "<JWT_REFRESH_TOKEN>"
}
```
**Response:**
```json
{
  "access": "<NEW_JWT_ACCESS_TOKEN>"
}
```

### Snippet APIs
#### 3. Create Snippet
**Endpoint:** `http://127.0.0.1:8000/api/snippets/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "title": "Sample Snippet",
  "note": "This is a sample snippet",
  "tags": ["Django", "API"]
}
```
**Response:**
```json
{
  "id": 1,
  "title": "Sample Snippet",
  "note": "This is a sample snippet",
  "tags": ["Django", "API"],
  "created_at": "2025-03-22T12:00:00Z"
}
```

#### 4. List Snippets
**Endpoint:** `http://127.0.0.1:8000/api/snippets/`  
**Method:** `GET`
**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample Snippet",
    "note": "This is a sample snippet",
    "tags": ["Django", "API"],
    "created_at": "2025-03-22T12:00:00Z"
  }
]
```

#### 5. Snippet Detail
**Endpoint:** `http://127.0.0.1:8000/api/snippets/{id}/`  
**Method:** `GET`

#### 6. Update Snippet
**Endpoint:** `http://127.0.0.1:8000/api/snippets/{id}/`  
**Method:** `PUT`

#### 7. Delete Snippet
**Endpoint:** `http://127.0.0.1:8000/api/snippets/{id}/`  
**Method:** `DELETE`

#### 8. List Tags
**Endpoint:** `http://127.0.0.1:8000/api/tags/`  
**Method:** `GET`

#### 9. Get Snippets by Tag
**Endpoint:** `http://127.0.0.1:8000/api/tags/{id}/`  
**Method:** `GET`

#### 10. Get Snippets by Overview
**Endpoint:** `http://127.0.0.1:8000/api/snippets/overview/`
**Method:** `GET`
**Response:**
```json
{
    "total_snippets": 3,
    "snippets": [
        {
            "id": 1,
            "title": "Python Basics",
            "detail_url": "http://127.0.0.1:8000/api/snippets/1/"
        },
        {
            "id": 2,
            "title": "Django Models",
            "detail_url": "http://127.0.0.1:8000/api/snippets/2/"
        },
        {
            "id": 3,
            "title": "React Hooks",
            "detail_url": "http://127.0.0.1:8000/api/snippets/3/"
        }
    ]
}
```

## Test Cases (cURL Examples)

### 1. Login
```bash
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'
```

### 2. Create a Snippet
```bash
curl -X POST http://127.0.0.1:8000/snippets/ -H "Authorization: Bearer <JWT_ACCESS_TOKEN>" -H "Content-Type: application/json" -d '{"title": "New Snippet", "note": "Snippet content", "tags": ["Python"]}'
```

### 3. List Snippets
```bash
curl -X GET http://127.0.0.1:8000/snippets/ -H "Authorization: Bearer <JWT_ACCESS_TOKEN>"
```

---

## Database Schema
```
User (Django default model)
    ├── id (PK)
    ├── username
    ├── password

Tag
    ├── id (PK)
    ├── title (Unique)

Snippet
    ├── id (PK)
    ├── title
    ├── note
    ├── created_at
    ├── updated_at
    ├── user (FK to User)
    ├── tags (Many-to-Many with Tag)
```

---

## Docker Deployment (Optional)

### 1. Build and Run with Docker
```bash
docker-compose up --build
```

### 2. Access the API
API will be available at `http://127.0.0.1:8000/`

---

## Postman Collection
A Postman collection is provided in the repository. Import `snipbox.postman_collection.json` into Postman to test APIs.

---

## Contributing
Feel free to submit a pull request if you would like to contribute to SnipBox!

---


