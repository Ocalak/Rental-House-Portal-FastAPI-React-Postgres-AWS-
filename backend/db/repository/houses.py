from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Float
import requests
from schemas.houses import HouseCreate
from db.models.houses import House
import requests
import pgeocode


def create_new_house(house: HouseCreate,db: Session,owner_id:int):
    house_object = House(**house.dict(),owner_id=owner_id)
    db.add(house_object)
    db.commit()
    db.refresh(house_object)
    return house_object

def retreive_house(id:int,db:Session):
    item = db.query(House).filter(House.id == id).first()
    return item

def update_house_by_id(id: int, house: HouseCreate, db: Session):
    existing_house = db.query(House).filter(House.id == id)
    if not existing_house.first():
        return 0
    house.__dict__.update(
        #owner_id=owner_id
    )  # update dictionary with new key value of owner_id
    existing_house.update(house.__dict__)
    db.commit()
    return 1

def list_houses(db: Session):
    houses = db.query(House).all()
    return houses


def delete_house_by_id(id: int,db: Session,owner_id):
    existing_house = db.query(House).filter(House.id == id)
    if not existing_house.first():
        return 0
    existing_house.delete(synchronize_session=False)
    db.commit()
    return 1



def create_new_hase(house: HouseCreate,db: Session,owner_id:int):
    house_object = House(**house.dict(),owner_id=owner_id)
    db.add(house_object)
    db.commit()
    db.refresh(house_object)
    return house_object 



def geolng(countrycode:str,zipcode:int,api_key:str):
    url = f"https://thezipcodes.com/api/v1/search?zipCode={zipcode}&countryCode={countrycode}&apiKey={api_key}"
    response = requests.get(url)
    json_data = response.json()
    lng=json_data['location'][0]['longitude']
    #lng = Float(lng)
    lat= float(json_data['location'][0]['latitude'])
    #lat=Float(lat)
    #return(json_data['location'][0]['latitude'],json_data['location'][0]['longitude'])
    return (lng)

def geolat(countrycode:str,zipcode:int,api_key:str):
    url = f"https://thezipcodes.com/api/v1/search?zipCode={zipcode}&countryCode={countrycode}&apiKey={api_key}"
    response = requests.get(url)
    json_data = response.json()
    
    lat= float(json_data['location'][0]['latitude'])
    #lat=Float(lat)
    #return(json_data['location'][0]['latitude'],json_data['location'][0]['longitude'])
    return (lat)

    
    

