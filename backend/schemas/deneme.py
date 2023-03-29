from fastapi import APIRouter,Response

from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from datetime import timedelta
from typing import Any
from fastapi import UploadFile,File,Form,Request,requests
import psycopg2
from botocore.exceptions import ClientError
from pydantic.types import constr,SecretStr
from typing import Optional ,List
from pydantic import BaseModel, Field 
from pydantic.networks import EmailStr
from datetime import date,datetime
import boto3
from db.models.users import User #new
from apis.version1.route_login import get_current_user_from_token  #new
from fastapi.middleware.cors import CORSMiddleware
import magic
from uuid import uuid4
from db.session import get_db
from db.models.houses import House
from schemas.houses import HouseCreate,ShowHouse,House,HouseUpdate
from db.repository.houses import create_new_house, retreive_house, update_house_by_id,list_houses, delete_house_by_id,create_new_hase
from loguru import logger
session1 = boto3.Session(
    aws_access_key_id='AKIAQPJD7WM6TR724UV2',
    aws_secret_access_key='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'
)
S3_BUCKET_NAME = "ocalak11"
s3 = session1.resource("s3")
bucket = s3.Bucket(S3_BUCKET_NAME)

KB= 1024
MB = 1024 *KB


SUPPORTED_FILE_TYPES = {
    'image/png': 'png',
    'image/jpeg': 'jpg'
}

async def s3_upload(contents:bytes,key:str):
    logger.info(f'Uploading {key} to S3')
    bucket.put_object(Key=key, Body=contents)




router = APIRouter()


'''@router.post("/create-house/",response_model=ShowHouse)
def create_house(house: HouseCreate,db: Session = Depends(get_db)):
    current_user = 1
    house = create_new_house(house=house,db=db,owner_id=current_user)
    return(house)'''

@router.post("/img-upload/")
async def upload(id:int,file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='No file found')
    contents= await file.read()
    size= len(contents)

    if not 0 < size <= 1 * MB:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Suppoerted file size is 0-1MB')

    file_type = magic.from_buffer(buffer=contents,mime=True)

    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail=f'Unsupported file type: {file_type}. Supported types are {SUPPORTED_FILE_TYPES}'
                           )

    await s3_upload(contents=contents, key=f'{id}.{SUPPORTED_FILE_TYPES[file_type]}')



@router.put("/update/{id}")
async def update_house(id: int, house: HouseCreate, db: Session = Depends(get_db),file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='No file found')
    contents= await file.read()
    size= len(contents)

    if not 0 < size <= 1 * MB:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Suppoerted file size is 0-1MB')

    file_type = magic.from_buffer(buffer=contents,mime=True)

    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail=f'Unsupported file type: {file_type}. Supported types are {SUPPORTED_FILE_TYPES}'
                           )

    await s3_upload(contents=contents, key=f'{id}.{SUPPORTED_FILE_TYPES[file_type]}')
    
    img_url = f'https://ocalak11.s3.eu-central-1.amazonaws.com/{id}.{SUPPORTED_FILE_TYPES[file_type]}'
    house.img_url = img_url
    




    message = update_house_by_id(id=id, house=house, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"House with id {id} not found"
        )
    return {"msg": "Successfully updated data."}