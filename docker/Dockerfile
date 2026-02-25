FROM python:3.13-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy Django app
COPY /app/ /app/

# Expose port
EXPOSE 8000

# Start with Gunicorn
CMD ["gunicorn", "student_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
