# Ngrok_learning

This project implements a FastAPI application with SQLAlchemy and Pydantic, following the layered architecture (routes, repositories, schemas, models).

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   - Copy `.env.example` to `.env` (already done as `.env`).
   - Update `DATABASE_URL` in `.env`.
   - For Vercel Postgres, use the connection string provided by Vercel.

## Running Locally

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API at `http://localhost:8000`.
3. Check the interactive docs: `http://localhost:8000/docs`.

## Deployment (Vercel)

1. Ensure `vercel.json` is present.
2. Deploy using Vercel CLI or Git integration.
3. Add `DATABASE_URL` environment variable in Vercel project settings.

## Project Structure

- `main.py`: Application entry point.
- `database.py`: Database connection setup.
- `models.py`: SQLAlchemy models (User).
- `schemas.py`: Pydantic schemas (UserCreate, UserResponse).
- `repositories/`: Database interaction logic.
- `routes/`: API route definitions.