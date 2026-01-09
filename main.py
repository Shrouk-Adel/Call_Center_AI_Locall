from fastapi import FastAPI
from app import health_router




app = FastAPI()

app.include_router(health_router)
