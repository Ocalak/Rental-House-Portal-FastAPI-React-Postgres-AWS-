from fastapi import APIRouter,Response
from numpy import float64
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
from db.session import get_db,engine
from db.models.houses import House as Hause
from schemas.houses import HouseCreate,ShowHouse,House,HouseUpdate
from db.repository.houses import create_new_house, retreive_house, update_house_by_id,list_houses, delete_house_by_id,create_new_hase
from loguru import logger
from db.models.photos import Photo
import requests
from db.repository.houses import geolat,geolng
from fastapi.encoders import jsonable_encoder
from apis.version1.sifre import api_key,countrycode
from fastapi.responses import HTMLResponse
from sqlalchemy import text,create_engine




session1 = boto3.Session(
    aws_access_key_id='xxxxx',
    aws_secret_access_key='xxxxx'
)
S3_BUCKET_NAME = "xxxx"
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



@router.post("/create-house/",response_model=ShowHouse)
def create_house(house: HouseCreate,db: Session = Depends(get_db)):
    current_user = 1
    house = create_new_house(house=house,db=db,owner_id=current_user)
    return(house)












@router.post("/img-upload/")
async def upload(houseid:int,username:str,file2: UploadFile = File(...),file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='No file found')
    contents= await file.read()
    size= len(contents)
    if not file2 :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='No file found')
    contents2= await file2.read()
    size2= len(contents2)
    if not 0 < size2 <= 1 * MB:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Suppoerted file size is 0-1MB')

    file_type2 = magic.from_buffer(buffer=contents2,mime=True)

    if not 0 < size <= 1 * MB:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Suppoerted file size is 0-1MB')

    file_type = magic.from_buffer(buffer=contents,mime=True)

    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail=f'Unsupported file type: {file_type}. Supported types are {SUPPORTED_FILE_TYPES}'
                           )
    if file_type2 not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail=f'Unsupported file type: {file_type2}. Supported types are {SUPPORTED_FILE_TYPES}'
                           )
    await s3_upload(contents=contents, key=f'{username}-{houseid}.{SUPPORTED_FILE_TYPES[file_type]}')
    await s3_upload(contents=contents2, key=f'{username}-{houseid}-2.{SUPPORTED_FILE_TYPES[file_type]}')
    uploaded_file_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{username}-{houseid}.{SUPPORTED_FILE_TYPES[file_type]}"
    uploaded_file_url2 = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{username}-{houseid}-2.{SUPPORTED_FILE_TYPES[file_type]}"
    existing_house = db.query(Hause).filter(Hause.id == houseid).first()
    existing_house.img_url = uploaded_file_url
    existing_house.img_url2 = uploaded_file_url2


    #lng= geolng(countrycode,existing_house.zipcode,api_key)
    #existing_house.lng = loc_house[0]
    #existing_house.lat = loc_house[1]



    
    #existing_house.lat = loc_house['latitude']
    #existing_house.lng = loc_house['longitude']

    db.add(existing_house)
    db.commit()
    db.refresh(existing_house)
    return existing_house

    
   


    





@router.get("/get/{id}",response_model=ShowHouse) # if we keep just "{id}" . it would stat catching all routes
def read_house(id:int,db:Session = Depends(get_db)):
    house = retreive_house(id=id,db=db)
    if not house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"House with this id {id} does not exist")
    return house


@router.get("/all-houses", response_model= List[ShowHouse])
def read_house(db:Session = Depends(get_db)):
    houses = list_houses(db=db)
    return houses

@router.put("/update/{id}")
def update_house(id: int, house: HouseCreate, db: Session = Depends(get_db)):
    #current_user = 1
    message = update_house_by_id(id=id,
                                  house=house, 
                                  db=db,
                                    #owner_id=current_user
                                    )
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"House with id {id} not found"
        )
    return {"msg": "Successfully updated data."}



  


'''@router.delete("/delete/{id}")
def delete_house(id: int,db: Session = Depends(get_db)):
    current_user_id = 1
    message = delete_house_by_id(id=id,db=db,owner_id=current_user_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"House with id {id} not found")
    return {"msg":"Successfully deleted."}'''


@router.delete("/delete/{id}")
def delete_house(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    house = retreive_house(id =id,db=db)
    if not house:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"House with {id} does not exist")
    print(house.owner_id,current_user.id,current_user.is_superuser)
    if house.owner_id == current_user.id or current_user.is_superuser:
        delete_house_by_id(id=id,db=db,owner_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")





@router.get("/search/")
async def search_houses(rent:int=None,
                        no_rooms:int=None,
                        size:int=None,
                        additional_cost:int=None,
                        total_rent:int=None,
                        max_flatmates:int=None,
                        heating_type:str=None,
                        heating_cost:int=None,
                        city:str=None,
                        min_duration:int=None,
                        #smoking_allowed:bool=None,
                        db:Session=Depends(get_db)):
    aka = db.query(Hause)
    if not rent:
       rent= 1000000
    if Hause.rent :
        aka = aka.filter(Hause.rent <= rent)
    if not min_duration:
       min_duration= 1000000
    if Hause.min_duration :
        aka = aka.filter(Hause.min_duration <= min_duration)

    if not no_rooms:
        no_rooms= 1000000
    if Hause.no_rooms :
        aka = aka.filter(Hause.no_rooms <= no_rooms)
    if not size:
        size = 1000000
    if Hause.size :
        aka = aka.filter(Hause.size <= size)
    if not additional_cost:
        additional_cost = 1000000
    if Hause.additional_cost :
        aka = aka.filter(Hause.additional_cost <= additional_cost)
    if not total_rent:
        total_rent = 1000000
    if Hause.total_rent :
        aka = aka.filter(Hause.total_rent <= total_rent)
    if not max_flatmates:
        max_flatmates = 1000000
    if Hause.max_flatmates :
        aka = aka.filter(Hause.max_flatmates <= max_flatmates)
    if heating_type is not None:
       # heating_type = Any
    #if Hause.heating_type :
        aka = aka.filter(Hause.heating_type == heating_type)
    if not heating_cost:
        heating_cost = 1000000
    if Hause.heating_cost :
        aka = aka.filter(Hause.heating_cost <= heating_cost)
    if city is not None:
    #if Hause.city :
        aka = aka.filter(Hause.city == city)
    #if smoking_allowed is not None:
        #aka.filter(Hause.smoking_allowed == smoking_allowed)
    result = aka.all()
    return result
 



#api="xxxxxx"





'''@router.get("/houses", response_class=HTMLResponse)
async def show_houses():
    return """
    <html>
        <head>
            <title>House Map</title>
            <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBEXsQDjR-U8jrI_K51JXb4enPHXevB2i0&callback=initMap"
            async defer></script>
            <script>
                function initMap() {
                    // Initialize the map
                    var map = new google.maps.Map(document.getElementById('map'), {
                        center: {lat: 51.404, lng: 6.4194},
                        zoom: 10
                    });
                    
                    // Fetch the houses from the backend
                    fetch('/api/houses/')
                        .then(response => response.json())
                        .then(data => {
                            // Loop through the houses and add markers to the map
                            data.forEach(house => {
                                var marker = new google.maps.Marker({
                                    position: {lat: house.lat, lng: house.lng},
                                    map: map,
                                    title: house.adress
                                });
                            });
                        });
                }
            </script>
        </head>
        <body>
            <div id="map" style="height: 500px;"></div>
        </body>
    </html>
    """

@router.get("api/houses",response_model=List[ShowHouse])
async def read_house(db:Session = Depends(get_db)):
     rows = list_houses(db=db)
     return [{"adress": row["adress"], "latitude": row["lat"], "longitude": row["lng"]}
            for row in rows]'''
