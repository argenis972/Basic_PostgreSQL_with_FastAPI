# User Management API (Mini-Lab)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-Passing-success?style=flat-square)

A streamlined RESTful API designed to explore **Clean Architecture principles** using FastAPI and PostgreSQL. This project focuses on the separation of concerns, ensuring a scalable structure even for small applications.

*While simplified, the project follows Clean Architecture principles by keeping HTTP, business logic and data access clearly separated.*

## 🎯 Key Concepts applied
* **Service Layer Pattern:** Decoupling business logic from API routes.
* **Database Management:** Raw SQL interactions via `psycopg2` for granular control.
* **Unit Testing:** Isolated testing strategy using `unittest.mock` (zero database dependency during tests).
* **Error Handling:** Centralized exception management.

---

## 🏗️ Project Structure
The architecture is modular, separating the entry point from logic and data access.

```text
app/
├── api/
│   └── usuarios.py       # Routes & HTTP handling
├── core/
│   └── config.py         # Application Configuration
├── db/
│   └── conexao.py        # Database Connection (Singleton pattern)
├── services/
│   └── usuarios.py       # Business Logic Layer
├── schemas/
│   └── usuarios.py       # Pydantic Models (Data Validation)
├── tests/
│   ├── test_usuarios.py
│   └── ...               # Mocks & Unit Tests
|
├── main.py               # Application Entry Point
├── .env                  # Environment Variables
├── .env.example          # Example Env File
├── .gitignore            # Git Ignore File
├── pytest.ini            # Pytest Configuration
├── README.md             # Project Documentation
└── requirements.txt      # Dependencies
```
## 🚀 Getting Started
### Prerequisites
- Python 3.12+
- PostgreSQL running locally

### 1. Database Setup
Execute the following SQL command in your PostgreSQL instance:
```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);
```
Note: Environment variables are loaded via .env. See .env.example

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/argenis972/Basic_PostgreSQL_with_FastAPI
pip install -r requirements.txt
```
### 3. Running the Server
```bash
uvicorn app.main:app --reload
```
The API will be available at: http://127.0.0.1:8000

## 📡 API Reference
Once the server is running, full interactive documentation (Swagger UI) is  available at: 👉 http://127.0.0.1:8000/docs

### Core Endpoints
| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/usuarios/` | Retrieve a list of all registered users. |
| `POST` | `/usuarios/` | Create a new user with the provided data. |

## Example Payload (POST):
```json
{
    "nome": "Marcus"
}
```
## 🧪 Testing
Run the test suite using:
```bash
python -m pytest
```
**Current Status:**
✅ 4 passed in 0.xx seconds

## 🔮 Roadmap & Future Improvements
While fully functional, this lab serves as a foundation for further complexity:
- [ ] Implement dependency injection for DB sessions.
- [ ] Add Database Transactions (Rollbacks).
- [ ] Dockerize the application.
- [ ] Transition to an ORM (SQLAlchemy) for comparison.
---
Created for learning purposes. Feedback is welcome.

## 👤 Author 

- **Argenis López** <br />

*Backend Developer — Python | FastAPI | PostgreSQL*

## 📬 Contact

- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

## 📜 License

MIT — Feel free to study, adapt, and evolve.








