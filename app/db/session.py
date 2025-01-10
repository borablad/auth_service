from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# Настройка подключения к базе данных
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
