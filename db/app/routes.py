from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema, Request, Response, RequestUser

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="user created successfully").dict(exclude_none=True)


@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@router.patch("/update")
async def update_user(request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.update_user(db, user_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_user)


@router.delete("/delete")
async def delete_user(request: RequestUser,  db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)