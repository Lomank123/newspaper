from fastapi import FastAPI
from src.routes import api_router


# FastAPI
app = FastAPI()

# Routing
app.include_router(api_router, prefix='/api/v1')
