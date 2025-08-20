from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.get("/", response_model=list[schemas.ProjectResponse])
def list_project(q: str |None  = Query(default=None), db:Session = Depends(database.get_db)):
    return crud.get_projects(db, q=q)

@router.post("/", response_model=schemas.ProjectResponse, status_code=201)
def create_project(payload: schemas.ProjectCreate, db: Session = Depends(database.get_db)):
    return crud.create_project(db, payload)

@router.get("/{project_id}", response_model=schemas.ProjectResponse)
def get_project(project_id: int, db: Session = Depends(database.get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    return project

@router.put("/{project_id}", response_model =schemas.ProjectResponse)
def update_project(project_id: int, payload: schemas.ProjectUpdate, db: Session = Depends(database.get_db)):
    project = crud.update_project(db, project_id, payload)
    if not project:
        raise HTTPException(404, "Project not found")
    return project


@router.delete("/{project_id}", status_code=204)
def delete_project(project_id: int, db: Session = Depends(database.get_db)):
    ok = crud.delete_project(db, project_id)
    if not ok:
        raise HTTPException(404, "Project not found")
    return 
