from sqlalchemy.orm import Session
from . import models, schemas

def create_book(db:Session, data:schemas.BookCreate, owner_id: int |None = None):
    book = models.Book(**data.model_dump(), owner_id=owner_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db:Session, q: str | None = None, limit: int = 50, offset: int = 0):
    query = db.query(models.Book)
    if q:
        like = f"%{q}%"
        query = query.filter(models.Book.title.ilike(like))

    return query.order_by(models.Book.id.desc()).offset(offset).limit(limit).all()

def get_book(db:Session, book_id:int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, data: schemas.BookUpdate):
    book = get_book(db, book_id)
    if not book:
        return None
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(book, k, v)

    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True



def create_project(db: Session, data:schemas.ProjectCreate, owner_id: int | None = None):
    project = models.Project(**data.model_dump(), owner_id = owner_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_projects(db: Session, q: str | None = None, limit: int = 50, offset: int = 0):
    query = db.query(models.Project)
    if q:
        like = f"%{q}%"
        query = query.filter(models.Project.title.ilike(like))
    return query.order_by(models.Project.id.desc()).offset(offset).limit(limit).all()

def get_project(db:Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def update_project(db:Session, project_id: int, data: schemas.ProjectUpdate):
    project = get_project(db, project_id)
    if not project:
        return None
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(project, k, v)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db:Session, project_id: int):
    project = get_project(db, project_id)
    if not project:
        return False
    db.delete(project)
    db.commit()
    return True


    