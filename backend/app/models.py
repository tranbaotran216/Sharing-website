from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    hashed_password= Column(String(128), nullable=False)
    books= relationship("Book", back_populates="owner")
    projects = relationship("Projects", back_populates="owner")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    author = Column(String(120))
    description = Column(Text, default="")
    file_url = Column(String(255))
    tags = Column(String(255))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="books")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, default="")
    tech_stack = Column(String(255))
    github_url = Column(String(255))
    demo_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="projects")