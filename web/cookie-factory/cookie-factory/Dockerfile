FROM mcr.microsoft.com/playwright/python:v1.41.2-jammy

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask playwright

RUN playwright install --with-deps chromium

EXPOSE 5000

CMD ["python", "app.py"]
