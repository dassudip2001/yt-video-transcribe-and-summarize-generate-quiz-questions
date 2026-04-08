# Langgrapth Backend (FastAPI)

This backend exposes an API that:
1. Downloads audio from a video URL (YouTube etc.) using `yt-dlp`
2. Transcribes the audio using OpenAI Whisper (`whisper-1`)
3. Summarizes the transcript with GPT-4o
4. Generates a quiz (MCQ + True/False + Short Answer) from the summary

## Requirements

- Python 3.11+
- An OpenAI API key

Environment variable:

- `OPENAI_API_KEY`

## Setup

1. `cd backend`
2. Copy/create `.env` (based on `backend/.env.example`)
3. Install dependencies:
   - `pip install -e .`

## Run

From the `backend/` directory:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:

- `http://localhost:8000/`
- `http://localhost:8000/generate`

## Endpoints

### GET `/`

Returns a health message.

### POST `/generate`

Generate a summary and quiz from a video URL.

Request body:

```json
{ "url": "https://www.youtube.com/watch?v=VIDEO_ID" }
```

Response (see `GenerateResponse`):

```json
{
  "summary": "string",
  "quiz": { "mcq": [], "true_false": [], "short_answer": [] } | null,
  "quiz_raw": "string|null",
  "parse_error": "string|null"
}
```

Notes:

- `quiz` is parsed from the model's JSON output. If parsing fails, `quiz` will be `null` and `parse_error` will be set.
- The downloaded audio is saved into the `backend/` directory as `<uuid>.<ext>`.

