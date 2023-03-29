from typing import Optional,List
from pydantic import BaseModel
from datetime import date,datetime
from fastapi import UploadFile, File
from pydantic import constr



#shared properties
class HouseBase(BaseModel):
    title : str
    rent : int
    no_rooms : int
    size : int
    additional_cost : int
    total_rent : int
    max_flatmates : int
    exist_fmates : int
    heating_type : str
    heating_cost : int
    city : str
    zipcode : int
    adress : str
    description : str
    min_duration : int
    smoking_allowed : bool
    parking : str
    postedby : str
    img_url: str
    img_url2: str
    lat:float
    lng:float
    is_active : bool
    date_posted : Optional[date] = datetime.now().date()
    
    
    
    
    

#this will be used to validate data while creating a Job
class HouseCreate(HouseBase):
    title : str
    rent : int
    no_rooms : int
    size : int
    additional_cost : int
    total_rent : int
    max_flatmates : int
    exist_fmates : int
    heating_type : str
    heating_cost : int
    city : str
    adress : str
    zipcode : int
    description : str
    min_duration : int
    smoking_allowed : bool
    parking : str
    postedby : str
    img_url: str
    img_url2:str
    lat:float
    lng:float
    is_active : bool
    date_posted : Optional[date] = datetime.now().date()
    
    

    
#this will be used to format the response to not to have id,owner_id etc
class ShowHouse(HouseBase):
    title : str
    rent : int
    no_rooms : int
    size : int
    additional_cost : int
    total_rent : int
    max_flatmates : int
    exist_fmates : int
    heating_type : str
    heating_cost : int
    city : str
    zipcode : int
    adress : str
    description : str
    min_duration : int
    smoking_allowed : bool
    parking : str
    postedby : str
    is_active : bool
    date_posted : date
    img_url: str
    img_url2 :str
    lat: float
    lng:float
   
  
    

    class Config():  #to convert non dict obj to json
        orm_mode = True
    

class HouseUpdate(HouseCreate):
   is_deleted: Optional[bool] = False

class House(HouseUpdate):
    profile_pc : Optional[str] = None
    house_name : Optional [constr(to_lower=True)]



