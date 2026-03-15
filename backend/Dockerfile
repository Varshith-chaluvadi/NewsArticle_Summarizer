FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for newspaper3k
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:7860", "--timeout", "120", "app:app"]
