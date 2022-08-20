FROM python:3.8.13-slim-bullseye

WORKDIR /app

RUN pip install --upgrade setuptools 

RUN pip install fastapi[all]

COPY . .

EXPOSE 8000:8000


CMD uvicorn app:app --reload --host 0.0.0.0 --port 8000