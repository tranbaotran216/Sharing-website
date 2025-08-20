from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.get("/", response_model=list[schemas.BookResponse])
def list_book(q: str | None = Query(default=None), db: Session = Depends(database.get_db)):
    return crud.get_books(db, q=q)

@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(payload: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, payload)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db:Session = Depends(database.get_db)):
    book = crud.get_book(db, book_id)
    if not book: 
        raise HTTPException(404, "Book not found")
    return book

#update
@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, payload: schemas.BookUpdate, db: Session = Depends(database.get_db)):
    book = crud.update_book(db, book_id, payload)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(database.get_db)):
    ok = crud.delete_book(db, book_id)
    if not ok:
        raise HTTPException(404, "Book not found")
    return 

