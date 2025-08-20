from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

class Bookbase(BaseModel):
    title: str
    author: Optional[str] = None
    description: Optional[str] = ""
    file_url: Optional[str] = None
    tags: Optional[str] = None

class BookCreate(Bookbase):
    pass

class BookUpdate(Bookbase):
    pass 

class BookResponse(Bookbase):
    id: int
    owner_id: Optional[int] = None
    class Config:
        orm_mode = True



class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = ""
    tech_stack : Optional[str]  = None
    git_hub_url: Optional[str] = None
    demo_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass 

class ProjectUpdate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    owner_id:  Optional[int] = None
    class Config:
        orm_mode = True