from fastapi import APIRouter
from src.api import mainPage

api_router = APIRouter()
api_router.include_router(mainPage.router, prefix="/mainPage", tags=["usuarios"])