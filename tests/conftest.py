import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.repositories.database import Base, get_db
from litestar import Litestar, get
from litestar.di import Provide
from src.controllers.irrigation_controller import get_irrigation_time


SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

# Создаём тестовую базу данных
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Фикстура для тестовой базы данных
@pytest.fixture(scope="session")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# Функция для переопределения зависимости get_db
async def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@get("/")
async def hello_world() -> str:
    return "Hello, Irrigation Service!"

# Создаём тестовое приложение с переопределённой зависимостью
@pytest.fixture(scope="session")
def test_app():
    route_handlers = [
        get_irrigation_time, 
        hello_world,
    ]
    test_app = Litestar(
        route_handlers=route_handlers,
        dependencies={"get_db": Provide(override_get_db, sync_to_thread=False)}
    )
    return test_app