FROM python:3.9-slim

WORKDIR /app
COPY pato_appka /app

RUN pip install flask

EXPOSE 5000
CMD ["python", "app.py"]
