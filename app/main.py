from fastapi import FastAPI
from app.api.endpoints import auth
from app.db.base import Base
from app.db.session import engine

# Инициализация базы данных
def init_db():
    Base.metadata.create_all(bind=engine)

# Создание приложения
app = FastAPI(
    title="Auth Service",
    description="Сервис авторизации для управления пользователями",
    version="1.0.0"
)

# Инициализация базы данных при старте
@app.on_event("startup")
def startup_event():
    init_db()

# Подключение маршрутов
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
