# routes/user.py
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from ..controllers import user
from ..models.user import User
from ..config.database import SessionLocal
from pydantic import BaseModel
import uuid

router = APIRouter(prefix="/user", tags=["User"])

class UserSchema(BaseModel):
    email: str
    password : str

@router.get("/getOne/{user_id}")
def get_user(user_id: uuid.UUID ):
    user_info = user.get_user(user_id)
    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info

@router.get("/getAll/{skip}/{limit}")
def get_all_users(skip: int = 0, limit: int = 10 ):
    print(skip,limit)
    return user.get_users(skip=skip, limit=limit)

@router.post("/create")
def create_user(userData : UserSchema ):
    # request.json() ile gelen JSON verisine erişebilirsiniz
    # print(email, username)
    return user.create_user(userData)

@router.post("/login")
def lgoin_user(userData : UserSchema ):
    # request.json() ile gelen JSON verisine erişebilirsiniz
    # print(email, username)
    return user.login_user(userData)

@router.put("/update/{user_id}")
def update_user(user_id: uuid.UUID, userData : UserSchema ):
    print("udapte", user_id, userData)

    # user_info = user.update_user(user_id=user_id, username=username, email=email)
    # if user_info is None:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return user_info

@router.delete("/delete/{user_id}")
def delete_user(user_id: uuid.UUID, ):
    user_info = user.delete_user(user_id=user_id)
    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info
