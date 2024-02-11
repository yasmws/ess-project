from fastapi import APIRouter
from backend.src.api import home

api_router = APIRouter()
api_router.include_router(home.router, prefix="/home")