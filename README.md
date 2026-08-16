# Restaurant POS

A traditional restaurant point-of-sale system built with FastAPI and PostgreSQL.

## Status

Early scaffolding. Database connection and app structure are in place; core features are still being built.

## Planned Features

- User login with role-based access control (RBAC)
- Seeded menu items and users
- Order lifecycle with state changes: `open` → `closed` → `paid`
- Tip handling
- Order total calculation (subtotal, tax, tip, grand total)

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **PostgreSQL** (Neon) — database
- **Pydantic Settings** — configuration management
- **psycopg2** — PostgreSQL driver

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```
   DATABASE_URL=your_postgres_connection_string
   SECRET_KEY=your_secret_key
   ENVIRONMENT=development
   ```
4. Run the app:
   ```
   uvicorn main:app --reload
   ```
5. Visit `http://localhost:8000` to confirm it's running, and `http://localhost:8000/test-db` to confirm the database connection.

## Project Structure

```
.
├── main.py           # FastAPI app entrypoint
├── config.py          # Pydantic settings
├── db/
│   └── session.py     # SQLAlchemy engine/session setup
├── requirements.txt
└── .env                # not committed
```
