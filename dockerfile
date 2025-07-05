# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional: psycopg2 needs these)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start the app with gunicorn
CMD ["gunicorn", "app/app:app"]
