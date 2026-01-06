# User Management API (Mini-Lab)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B_(tested%20with%2016)-336791?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-Passing-success?style=flat-square)

A lean RESTful API to study **backend best practices** and clean separation of concerns with FastAPI + PostgreSQL (routes → schemas → services → database).

> The project is intentionally small, but structured to scale without becoming hard to maintain.

## 🎯 Concepts applied
- **Service Layer Pattern:** business logic separated from HTTP routes.
- **PostgreSQL with psycopg (v3) + Pool:** efficient connections with full control using raw SQL.
- **Environment-based settings (.env):** centralized configuration via `pydantic-settings` using a single `DATABASE_URL`.
- **Unit tests with mocks:** fast and isolated tests (no database dependency during `pytest`).
- **Logging:** structured logs with stacktraces for easier debugging.

---

## 🏗️ Project Structure

```text
app/
├── api/
│   └── usuarios.py        # Routes and HTTP layer
├── core/
│   ├── config.py          # Environment settings (ENV, DATABASE_URL, LOG_LEVEL)
│   └── logging.py         # Logging setup
├── db/
│   ├── pool.py            # Connection pool (psycopg_pool)
│   └── __init__.py
├── services/
│   └── usuarios.py        # Service layer (rules + DB access)
├── schemas/
│   └── usuarios.py        # Pydantic models (input/output)
├── tests/
│   ├── conftest.py
│   ├── test_usuarios.py
│   └── ...                # Mocks & unit tests
|
├── main.py                # Application entry point
├── .env                   # Environment variables (DO NOT commit)
├── .env.example           # Example env file
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- PostgreSQL **14+ (tested with 16)** running locally (Windows)

### 1) Database table (manual for now)
Connect to the same database defined in your `DATABASE_URL` and run:

```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);
```

> Note: table creation is currently manual for didactic simplicity. Migrations (Alembic) are planned in the roadmap.

### 2) Environment variables
Create a `.env` file in the project root (use `.env.example` as reference):

```env
ENV=dev
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/postgres
LOG_LEVEL=INFO
```

If your password contains special characters, you may need URL encoding. Example:

```env
DATABASE_URL=postgresql://postgres:senha%40123@localhost:5432/postgres
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the server
```bash
uvicorn app.main:app --reload
```

API base URL: http://127.0.0.1:8000

---

## 📡 API Documentation (Swagger)
Once the server is running:
👉 http://127.0.0.1:8000/docs

---

## 🔌 Endpoints

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| GET    | `/usuarios` | List all users |
| POST   | `/usuarios` | Create a user |

### Example payload (POST)
```json
{
  "nome": "Marcus"
}
```

---

## 🧪 Testing
Run the test suite with:

```bash
python -m pytest
```

Note: the current test suite is **unit-based and uses mocks**, so it does not require a running database to pass.

---

## 🧾 Logging
Logging is configured in a centralized way with an environment-driven log level (via `LOG_LEVEL`).

---

## 🔮 Roadmap (next practical steps)
- [ ] Add migrations (Alembic) to remove manual SQL setup.
- [ ] Add integration tests against a real PostgreSQL database (in addition to mocks).
- [ ] Add CI with GitHub Actions (pytest + lint).
- [ ] Improve global exception handling (centralized error responses).

---

## 👤 Author
- **Argenis López**

Backend Developer — Python | FastAPI | PostgreSQL

## 📬 Contact
- LinkedIn: https://www.linkedin.com/in/argenis972/
- E-mail: argenislopez28708256@gmail.com
- GitHub: https://github.com/argenis972

## 📜 License
MIT — Feel free to study, adapt, and evolve.








