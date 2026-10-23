# Course Catalog API

A REST API for the course catalog, built with FastAPI and Pydantic.

## How to run

```bash
cd course-catalog-api
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate        # macOS / Linux
pip install -r requirements.txt
fastapi dev main.py
```

Open http://127.0.0.1:8000/docs for interactive documentation.

## What changed in Lab 5

- CORS enabled for `http://localhost:3000` — required so the browser can send requests from the Next.js frontend to a different origin (port 8000)
- camelCase JSON via `CamelModel` with `alias_generator=to_camel` — frontend `Course` type uses `isElective`, backend Python uses `is_elective`; Pydantic translates automatically
- `POST /courses/{course_id}/like` — increments likes counter, returns updated course
- `POST /enrollments` — accepts `{ courseId, studentName }`, returns `{ id, courseId, studentName }` with status 201; validates `studentName` min 2 chars
- `GET /enrollments` — lists all in-memory enrollments

## What was verified

| Request | Result |
|---|---|
| `GET /` | `{"message": "Course Catalog API is running"}` |
| `GET /courses` | 6 courses, camelCase keys, ai-integration first (32 likes) |
| `GET /courses?is_elective=true` | 2 courses: ai-integration, api-design |
| `GET /courses?is_elective=false` | 4 courses |
| `GET /courses?sort=title` | 6 courses alphabetically |
| `GET /courses?page=2&page_size=2` | web-security, backend-fastapi |
| `GET /courses/web-security` | web-security course object |
| `GET /courses/nope` | 404 `{"detail": "Course not found"}` |
| `POST /courses/web-security/like` | 200, likes incremented |
| `POST /courses/nope/like` | 404 |
| `POST /enrollments` valid body | 201, enrollment with id |
| `POST /enrollments` name "A" | 422, validation error |
| `POST /enrollments` unknown course | 404 |
| `GET /enrollments` | list of enrollments |
