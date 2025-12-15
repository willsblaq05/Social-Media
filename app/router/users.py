from fastapi import Response, status, HTTPException, Depends,APIRouter
from .. import models, schemas,utils
from sqlalchemy.orm import Session
from typing import  List
from ..database import  get_db
router = APIRouter(
    tags=["Users"],
    prefix="/users"
)
@router.post("/",response_model= schemas.UserOut,
              status_code=status.HTTP_201_CREATED)
def create_user(user : schemas.CreateUser, db:Session=Depends(get_db)):
    hashed_password = utils.get_hash(user.password)
    user_dict = user.dict()
    user_dict['password'] = hashed_password
    new_user = models.User(**user_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/{id}", response_model=schemas.UserOut, status_code=status.HTTP_200_OK)
def get_user(id:int , db:Session =Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} was not found")
    return user
             


