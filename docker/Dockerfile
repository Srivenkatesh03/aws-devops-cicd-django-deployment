FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY /app/ /app/


EXPOSE 8000

# Start with Gunicorn
CMD ["gunicorn", "student_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
