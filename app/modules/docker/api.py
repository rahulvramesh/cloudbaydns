from typing import Any

from fastapi import APIRouter

router = APIRouter(
    prefix="/docker",
    tags=["docker"],
    responses={404: {"description": "Not found"}},
)


@router.post("/run")
async def update_admin() -> Any:
    return {"message": "Serverless Function Running"}
