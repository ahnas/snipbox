# 📝 SnipBox Backend API

SnipBox is a short note-saving application that allows users to store text snippets, organize them with tags, and manage them via a REST API. This backend is built using **Django Rest Framework (DRF)** with **JWT authentication**.

## 🌟 Features
- Save and manage snippets
- Tag-based organization
- JWT authentication
- API documentation with Swagger
- Docker deployment support (optional)

---

## 🚀 Getting Started

### 1⃣ Prerequisites
Ensure you have the following installed:
- **Python 3.12+**
- **PostgreSQL or SQLite**
- **pip** (Python package manager)
- **Virtual Environment** (recommended)

### 2⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/snipbox.git
cd snipbox
```

### 3⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 4⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5⃣ Set Up the Database
Apply migrations:
```bash
python manage.py migrate
```

Create a superuser:
```bash
python manage.py createsuperuser
```

### 6⃣ Run the Development Server
```bash
python manage.py runserver
```
API will be available at: **`http://127.0.0.1:8000`**

---

## 📝 API Documentation

### 🔹 **Authentication APIs**
| Method | Endpoint                 | Description |
|--------|--------------------------|-------------|
| `POST` | `/api/auth/login/`       | User login using JWT |
| `POST` | `/api/auth/refresh/`     | Refresh JWT token |

### 🔹 **Snippet APIs**
| Method  | Endpoint                  | Description |
|---------|---------------------------|-------------|
| `GET`   | `/api/snippets/`          | List all snippets |
| `POST`  | `/api/snippets/`          | Create a snippet |
| `GET`   | `/api/snippets/{id}/`     | Retrieve a snippet |
| `PUT`   | `/api/snippets/{id}/`     | Update a snippet |
| `DELETE`| `/api/snippets/{id}/`     | Delete a snippet |

### 🔹 **Tag APIs**
| Method  | Endpoint                  | Description |
|---------|---------------------------|-------------|
| `GET`   | `/api/tags/`              | List all tags |
| `GET`   | `/api/tags/{id}/`         | List snippets for a tag |

---

## 💑 API Documentation with Swagger
Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  

```

## 🧪 Running Tests
To test all API endpoints:
```bash
python manage.py test
```
Or run specific tests:
```bash
python manage.py test snippets.tests
```

