# Patient Management API

A REST API for managing patient records, built with FastAPI, SQLModel, and SQLite. Supports JWT authentication for write operations.

## Requirements

- Python 3.11+

## Installation

```bash
git clone <repo-url>
cd task3

python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

## Environment Setup

```bash
cp .env.example .env
```

Open `.env` and set a real secret key:

SECRET_KEY=your-long-random-secret-here

Generate one with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## Running the API

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for interactive documentation.

## Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /health | — | Health check |
| POST | /auth/register | — | Register a user |
| POST | /auth/token | — | Login, get JWT token |
| GET | /patients | — | List patients |
| GET | /patients/{id} | — | Get single patient |
| POST | /patients | ✅ | Create patient |
| PUT | /patients/{id} | ✅ | Full update |
| PATCH | /patients/{id} | ✅ | Partial update |
| DELETE | /patients/{id} | ✅ | Delete patient |

## Project Structure


## Reflection

**1. What does a path operation (endpoint) actually do when a request arrives?**

When a request arrives, FastAPI matches the URL and method to the correct function via the decorator (e.g. `@router.post("/patients")`). Before calling the function, FastAPI automatically validates the request body against the Pydantic model, resolves all dependencies (`Depends`), and extracts path/query parameters. If validation fails it returns 422 automatically. If everything passes, your function runs, does its DB work, and returns a Python object which FastAPI converts to JSON.

**2. Why use Pydantic response models instead of returning raw dicts?**

Response models guarantee what goes out of your API. They strip sensitive fields (like `hashed_password` via `UserRead`), validate the output shape, and auto-generate accurate OpenAPI docs. Raw dicts have no guarantees — you could accidentally expose internal fields or return inconsistent shapes.

**3. What is dependency injection and where did you use it?**

Dependency injection means a function declares what it needs and FastAPI provides it — instead of the function creating it itself. I used it in two places: `Depends(get_session)` injects a DB session into every endpoint, and `Depends(get_current_user)` injects the logged-in user into protected endpoints (and raises 401 if no valid token). This makes endpoints clean, testable, and reusable.

**4. How does JWT authentication work in your API, step by step?**

1. User registers via `POST /auth/register` — password is hashed and saved to DB
2. User logs in via `POST /auth/token` — password is verified, a JWT token is created with the username inside and returned
3. Client stores the token and sends it in every protected request: `Authorization: Bearer <token>`
4. `oauth2_scheme` extracts the token from the header automatically
5. `get_current_user` decodes the token, extracts the username, looks up the user in DB
6. If valid, the user object is injected into the endpoint and the request proceeds
7. If invalid or expired, 401 is returned

**5. What was the hardest bug you hit, and how did you debug it?**

The hardest bug was `if User is None` instead of `if user is None` in `get_current_user`. The capital `User` refers to the class itself which is never None, so the safety check never fired — meaning a valid token for a deleted user would crash instead of returning a clean 401. It was caught by writing a test for that specific case, which failed and pointed directly to the line. Secondly, i was totally caught by the syntax of test code that was supposed to be performed on the code.

**6. What would you add or change to make this API production-ready?**

To get this API ready for real-world use, the first step is moving from SQLite to PostgreSQL so the app can handle multiple users at the same time. We will also need Alembic to manage database updates safely. On the security side, we should add rate limiting to the login routes to stop password guessing, enforce HTTPS, shorten token lifespans, and configure CORS so only our official frontend can access the data. Finally, to keep the app fast as it grows, we need to add pagination to the patients list (loading data in smaller chunks) and set up better error logging so we can easily track down bugs.