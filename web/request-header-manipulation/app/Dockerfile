# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS builder

WORKDIR /app

COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["python3", "app.py"]
