import asyncio
import uvicorn
from src.sql.connection import create_tables_and_rows
from config import HOST, PORT
from src.custom_router import CustomRouter
from src.routes.statistic import router as statistic_router

CRoute = CustomRouter(
    statistic_router,
    title="Statistics API",
    version="1.0.1",
    description="Апи для тестового задания",
)


if __name__ == "__main__":
    asyncio.run(create_tables_and_rows())
    uvicorn.run(CRoute.app, host=HOST, port=PORT, log_level="info")
