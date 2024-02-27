# controllers/user.py
from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..config.database import SessionLocal
from ..models.user import User
from ..utils.jwt import create_access_token
from datetime import timedelta



def login_user(user : object, db: Session = SessionLocal()):
    logged_user = db.query(User).filter_by(email=user.email, password=user.password).first()
    if logged_user == None :
        raise HTTPException(status_code=404, detail="User not found")

    print("loginuser", logged_user)

    accessToken = create_access_token({"email" : logged_user.email, "id" :  str(logged_user.id)}, timedelta(weeks=2) )
    return {"access_token":accessToken, "access" : "Denied"}

def get_user(user_id: int, db: Session = SessionLocal()):
    return db.query(User).filter(User.id == user_id).first()

def get_users(skip: int = 0, limit: int = 10, db: Session = SessionLocal()):
    users = db.query(User).offset(skip).limit(limit).all()
    total_users = db.query(User).count()  # Toplam kullanıcı sayısını al
    return {"data": users, "total": total_users}

def create_user(user : object, db: Session = SessionLocal()):
    print("user" , user)
    new_user = User( email=user.email, password=user.password,)
    print("new_user", new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(user_id: int, username: str, email: str, db: Session = SessionLocal()):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        user.email = email
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(user_id: int, db: Session = SessionLocal()):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None