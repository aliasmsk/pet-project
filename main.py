import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

# Получаем настройки подключения к БД из переменных окружения (ENV)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


@app.get("/")
def read_root():
    """Простой эндпоинт для проверки работы приложения (Health Check)"""
    return {"status": "ok", "message": "App is running!"}


@app.get("/db-check")
def check_db():
    """Эндипоинт, который пробует подключиться к PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        conn.close()
        return {"database": "connected", "status": "success"}
    except Exception as e:
        return {"database": "error", "details": str(e)}
