from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")


@app.get("/")
def read_root():
    return {"Hello": "World"}
