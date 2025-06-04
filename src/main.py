from litestar import Litestar, get
from litestar.di import Provide
from src.repositories.database import get_db
from src.controllers.irrigation_controller import get_irrigation_time

@get("/")
async def hello_world() -> str:
    return "Hello, Irrigation Service!"

app = Litestar(
    route_handlers=[hello_world, get_irrigation_time],
    dependencies={"get_db": Provide(get_db, sync_to_thread=False)}
)