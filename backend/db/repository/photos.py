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


import boto3


import magic

from db.session import get_db



from loguru import logger
from db.models.photos import Photo
from schemas.photos import PhotoCreate


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

async def s3_download(key=str):
    try :
        return s3.Object(bucket_name=S3_BUCKET_NAME,key=key).get()['Body'].read()
    except ClientError as err: 
        logger.error(str((err)))


router = APIRouter()



def create_new_photo(photo:PhotoCreate,db:Session,img_url:str):
    photo_obj = Photo(**photo.dict(),img_url=img_url)
    
    db.add(photo_obj)
    db.commit()
    db.refresh(photo_obj)
    return photo_obj





'''@router.post("/img-upload/")
async def upload(house_id:int,owner_username:str,file: UploadFile = File(...),db:Session=Depends(get_db)):
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

    await s3_upload(contents=contents, key=f'{owner_username}-{house_id}.{SUPPORTED_FILE_TYPES[file_type]}')
    uploaded_file_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{owner_username}-{house_id}.{SUPPORTED_FILE_TYPES[file_type]}"
    
    photo =create_new_photo(photo=photo,db=db,img_url=uploaded_file_url)
    return photo
    
   
    
    #bucket.upload_fileobj(file.file, file.filename, ExtraArgs={"ACL": "public-read"})
    #uploaded_file_url = f"https://{S3_BUCKET_NAM'''