# Langgrapth

Langgrapth is a small app that generates a lesson summary and quiz from a video URL.

## Backend (FastAPI)

See `backend/README.md` for the full setup and API details.

Quick start:

```bash
cd backend
pip install -e .

# create backend/.env with:
# OPENAI_API_KEY=...
cp .env.example .env

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API:

- `POST http://localhost:8000/generate` with JSON: `{ "url": "..." }`

## Frontend (Next.js)

The `client/` folder contains a Next.js app.

Run it:

```bash
cd client
npm install
npm run dev
```

The UI page is currently minimal; connect it to the backend `POST /generate` endpoint when ready.

