## RealEstatePlatform-DRF-Swagger-scraper
# RealEstateAPI with JWT authentication and Swagger integration
---

# 🏠 RealEstateAPI

A Django Rest Framework (DRF) project to manage Real Estate property listings with full **JWT Authentication**, **CRUD operations**, **filter/search**, **image upload**, and **Swagger API Documentation**.

![Django](https://img.shields.io/badge/Django-4.2-green)
![DRF](https://img.shields.io/badge/DRF-3.14-blue)
![JWT](https://img.shields.io/badge/JWT-enabled-brightgreen)

---

## 📚 Table of Contents

- [Features](#-features)
- [Setup Instructions](#-setup-instructions)
- [JWT Authentication](#-jwt-authentication)
- [User Registration](#-user-registration)
- [Property API Endpoints](#-property-api-endpoints)
- [API Documentation](#-api-documentation-swagger--redoc)
- [Media Uploads](#-media-uploads)
- [Tech Stack](#-tech-stack)
- [License](#-license)

---

## 📦 Features

* 🔐 JWT Authentication (Login, Refresh)
* 🧑‍💻 User Registration
* 📄 CRUD APIs for Property
* 🔎 Filter by `location`, `price`
* 🔍 Search by `title`, `description`
* 📤 Image Upload Support
* 📃 Swagger & ReDoc Documentation

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ainy07/RealEstatePlatform-DRF-Swagger-scraper.git
cd RealEstatePlatform-DRF-Swagger-scraper


### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run the Server

```bash
python manage.py runserver
```

---

## 🔑 JWT Authentication

### Obtain Token

`POST /api/token/`

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

Response:

```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

### Refresh Token

`POST /api/token/refresh/`

```json
{
  "refresh": "your-refresh-token"
}
```

---

## 👤 User Registration

`POST /api/auth/register/`

```json
{
  "username": "newuser",
  "email": "email@example.com",
  "first_name": "First",
  "last_name": "Last",
  "password": "Password123!",
  "password2": "Password123!"
}
```

---

## 🏠 Property API Endpoints

**Base URL**: `/api/properties/`

> Use your JWT access token in Postman:
> `Authorization: Bearer <your-access-token>`

---

### ➕ Create Property

`POST /api/properties/`

**Headers:**

* `Content-Type: multipart/form-data`
* `Authorization: Bearer <access-token>`

**Body (Form-Data):**

| Key         | Value                    |
| ----------- | ------------------------ |
| title       | Luxury Apartment         |
| location    | Bangalore                |
| price       | 15000000                 |
| area\_sqft  | 1200                     |
| description | Spacious sea-facing flat |
| image       | (upload file)            |

---

### 📄 List Properties

`GET /api/properties/`

**Optional filters:**

```
/api/properties/?location=Bangalore&price=15000000
```

---

### 📃 Retrieve Property

`GET /api/properties/<id>/`

---

### ✏️ Update Property

`PUT /api/properties/<id>/`

**Headers:**

* `Authorization: Bearer <access-token>`

**Body (JSON):**

```json
{
  "title": "Updated Apartment",
  "location": "Delhi",
  "price": 20000000,
  "area_sqft": 1600,
  "description": "Updated description"
}
```

---

### ❌ Delete Property

`DELETE /api/properties/<id>/`

**Headers:**

* `Authorization: Bearer <access-token>`

---

## 🧪 API Documentation (Swagger & ReDoc)

* Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
* Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 📁 Media Uploads

Uploaded images are stored in the `/media/property_images/` directory.

Update `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

In `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧠 Tech Stack

* Python 3.9+
* Django 4.2+
* Django REST Framework
* JWT (Simple JWT)
* drf-yasg (Swagger)
* SQLite (Default DB)

---

## 📜 License

This project is licensed under the MIT License.

```

---

Would you like this saved and downloadable as a file (`README.md`) or committed to a GitHub repo?
```
