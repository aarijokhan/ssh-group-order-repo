FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip3 install poetry

COPY backend/pyproject.toml backend/poetry.lock* ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY backend/ .

RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
