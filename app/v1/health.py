from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["System"])


@router.get("/health")
async def health_check():
    return {
        "status": "Ok",
        "app": settings.APP_NAME,
        "version": "0.1.0",
    }