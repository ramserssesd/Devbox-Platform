Devbox Platform Backend - Setup Instructions
1). User Login with token generation
2). User Profile retrieval
3). API Usage Tracking
  - View past API usage
  - Create a new API usage entry
Swagger/OpenAPI documentation
Token Authentication

Technology
1). Python 3.8+
2) Django 4.x
3). Django REST Framework
4). drf-yasg (Swagger)
5). SQLite (in-memory, no persistence required)

Installation & Setup
1. Clone the repository
git clone https://github.com/ramserssesd/Devbox-Platform.git
cd Decbox-Platform
2. Create a virtual environment
python -m venv env
source env/bin/activate
3. Install dependencies
4. Run migrations
python manage.py makemigrations
python manage.py migrate
5. Create a superuser
python manage.py createsuperuser
6. Start the development server
python manage.py runserver

Authentication
All protected endpoints use Token Authentication.

1. First, login using:
POST /login/
{
  "username": "1234",
  "password": "1234"
}

2. Once login exutute you will get a token. that token top side the corner provide that one you will get all access to differnt endpoints.Use the returned token to access /profile/ and /api-usage/ like this:
Authorization: Token enter_login_token

Swagger API Docs
Visit: http://127.0.0.1:8000/swagger/
API Endpoints Summary

| Method | Endpoint         | Description                  |
| POST   | /login/          | Authenticate and return token |
| GET    | /profile/        | View user profile (requires token) |
| GET    | /api-usage/      | List user's API usage history |
| POST   | /api-usage/      | Log new API usage entry       |
