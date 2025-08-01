FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app


CMD sh -c "echo 'Iniciando aplicação FastAPI...' && uvicorn app.main:app --host 0.0.0.0 --port 8000"
