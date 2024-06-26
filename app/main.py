from fastapi import FastAPI

from app.configs.config import settings
from app.routers.route_include import router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Your API Works"}
