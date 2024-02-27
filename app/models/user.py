# models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from  ..config.database import Base
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, index=True)
    password = Column(String, index=True)
