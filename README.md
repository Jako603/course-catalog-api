# Course Catalog API

A REST API for the course catalog, built with FastAPI and Pydantic.

## How to run

```bash
cd course-catalog-api

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate        # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Start dev server
fastapi dev main.py
```

Open http://127.0.0.1:8000/docs for interactive documentation.

## What was verified

| Request | Result |
|---|---|
| `GET /` | `{"message": "Course Catalog API is running"}` |
| `GET /courses` | 6 courses, ai-integration first (32 likes) |
| `GET /courses?is_elective=true` | 2 courses: ai-integration, api-design |
| `GET /courses?is_elective=false` | 4 courses: modern-frontend, web-security, backend-fastapi, databases-postgresql |
| `GET /courses?sort=title` | 6 courses alphabetically by title |
| `GET /courses?page=1&page_size=2` | ai-integration, modern-frontend |
| `GET /courses?page=2&page_size=2` | web-security, backend-fastapi |
| `GET /courses?page=3&page_size=2` | databases-postgresql, api-design |
| `GET /courses?page=4&page_size=2` | `[]` |
| `GET /courses/web-security` | web-security course object |
| `GET /courses/nope` | 404 `{"detail": "Course not found"}` |
