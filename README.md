# 🛡️ User Signup & JWT Auth API (FastAPI)

This is a simple and secure backend API built using **FastAPI** for handling user registration, login, password hashing, and JWT-based authentication.

---

## 🚀 Features

- ✅ User Signup with Email Validation
- 🔐 Password Hashing using `passlib`
- 🔓 JWT Token Generation on Login
- 📧 Email format validation (`EmailStr`)
- 🔒 Protected endpoints using OAuth2 Bearer Token
- 🗃️ SQLite Database (with SQLAlchemy ORM)
- 📂 Environment-based configuration (`.env` support)

---

## 📁 Project Structure

- user_signup_project/
- main.py # FastAPI app entry point
- models.py # Pydantic models & DB models
- database.py # Database setup (SQLAlchemy + SQLite)
- utils.py # Utility functions (hashing, JWT)
- auth.py # JWT creation & token handling
- .env # Environment variables


---

## 🧪 Installation & Running

### 1️⃣ Clone the repo

```bash
git clone https://github.com/vinay-dev95/user_signup_project.git
cd user_signup_project

 uvicorn main:app --host 0.0.0.0 --port 8000 --reload

 Dependencies
fastapi

uvicorn

python-dotenv

passlib[bcrypt]

sqlalchemy

pydantic

python-jose (for JWT)

