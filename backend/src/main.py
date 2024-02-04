from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router import api_router
app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return "Server running!!"
