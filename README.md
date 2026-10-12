# User Management REST API

A Python backend application built with FastAPI for managing user records through RESTful API endpoints.

The project demonstrates core backend development concepts, including CRUD operations, request validation, relational database integration, and HTTP error handling.

## Tech Stack

- **Python** — Backend programming
- **FastAPI** — REST API framework
- **SQLAlchemy** — Database ORM
- **SQLite** — Relational database
- **Pydantic** — Request validation
- **Uvicorn** — ASGI server

## Features

- Create and retrieve user records
- Retrieve individual users by ID
- Update user information using PUT and PATCH
- Delete existing users
- Persist user records in SQLite
- Validate request data with Pydantic
- Return HTTP 404 errors for nonexistent users
- Access interactive API documentation through Swagger UI

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/users` | Create a user |
| GET | `/users` | Retrieve all users |
| GET | `/users/{user_id}` | Retrieve a user by ID |
| PUT | `/users/{user_id}` | Update a user |
| PATCH | `/users/{user_id}` | Partially update a user |
| DELETE | `/users/{user_id}` | Delete a user |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/karanehzm/first-fastapi-project.git
cd first-fastapi-project
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The application will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## Example Request

Create a user:

```http
POST /users
Content-Type: application/json
```

```json
{
  "id": 1,
  "name": "Alice",
  "age": 25
}
```

Partially update a user:

```http
PATCH /users/1
Content-Type: application/json
```

```json
{
  "age": 26
}
```

## Project Structure

```text
first-fastapi-project/
├── main.py        # API endpoints and request models
├── database.py    # Database engine and session configuration
├── models.py      # SQLAlchemy database model
└── .gitignore
```

The SQLite database file is created locally when the application starts.

## Future Improvements

- Automated tests using pytest
- Dependency-managed database sessions
- Improved error handling and input validation
- Authentication and authorization
- Containerization with Docker

## Author

Karaneh Zolfaghari Moghaddam

[GitHub](https://github.com/karanehzm)
