from fastapi import FastAPI, Depends

from .dependencies import get_query_token, get_token_header
from .routers import items, users

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    dependencies=[Depends(get_query_token)]
)

app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
def root():
    return {"message": "Hello Bigger Applications!"}
