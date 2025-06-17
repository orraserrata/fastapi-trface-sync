FROM python:3.11-slim

WORKDIR /app

# Gerekli sistem paketleri: gcc, git, build tools
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    build-essential \
    libffi-dev \
    libssl-dev \
    && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
