from litestar import get
from litestar.response import Response
from src.services.irrigation_service import IrrigationService


@get("/irrigation")
async def get_irrigation_time(soil_moisture: float, crop_type: str) -> Response:
    service = IrrigationService()
    time = service.calculate_irrigation_time(soil_moisture, {"temp": 25.0}, crop_type)
    return Response(content={"irrigation_time": time}, status_code=200)
