from fastapi import APIRouter,status, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils,oauth2
router = APIRouter(
    tags=["Authentication"]
)
@router.post("/login", response_model=schemas.Token )
def login(user_credetials: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credetials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    if not utils.auth(user_credetials.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
    #CREATE TOKEN
    #RETURN TOKEN
    access_token = oauth2.create_access_token(data = {"user_id":user.id,})
    return {"access_token":access_token, "token_type":"bearer" }

