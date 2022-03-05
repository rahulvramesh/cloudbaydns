from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import models, schemas
from app.core.config import settings

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# @router.post("/", response_model=schemas.User)  # type: ignore
# def create_user(
#         *,
#         db: Session = Depends(deps.get_db),
#         user_in: schemas.UserCreate,
#         current_user: models.User = Depends(deps.get_current_active_superuser),
# ) -> Any:
#     """
#     Create new user.
#     """
#     user = crud.user.get_by_email(db, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this username already exists in the system.",
#         )
#     user = crud.user.create(db, obj_in=user_in)
#     if settings.EMAILS_ENABLED and user_in.email:
#         send_new_account_email(
#             email_to=user_in.email, username=user_in.email, password=user_in.password
#         )
#     return user
