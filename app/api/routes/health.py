from core import Settings
from fastapi import APIRouter

settings = Settings()

health_router = APIRouter(
    prefix="/health",
    tags=["Health Check"],
)

@health_router.get("/", summary="Health Check Endpoint")
def health_check():
    print("Health check endpoint called")
    return {"status": "healthy",
            "app_name": settings.APP_NAME,
            "app_version": settings.APP_VERSION
            }