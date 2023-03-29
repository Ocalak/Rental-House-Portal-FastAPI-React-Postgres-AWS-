from fastapi import APIRouter, File, UploadFile,HTTPException, status,security
from sqlalchemy.orm import Session
from fastapi import Depends
from pydantic import BaseModel
from schemas.users import UserCreate,ShowUser
from db.session import get_db
from db.models.users import User
from db.repository.users import create_new_user, list_users
from fastapi_login import LoginManager
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from typing import List


router = APIRouter()



@router.post("/",response_model= ShowUser)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 

@router.get("/all-user", response_model= List[ShowUser])
def read_user(db:Session = Depends(get_db)):
    users = list_users(db=db)
    return users








'''@router.post("/uploadhouse/", status_code=201)
async def create_upload_file(properties: UserCreate, file: UploadFile = File(...)):
    return {"filename": file.filename, 'house': properties}'''

'''@router.post('/house')
async def upload(user: UserCreate = Depends(), file: UploadFile = File(...)):
    data_db = user.dict()
    print(data_db)'''

