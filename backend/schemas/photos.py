from typing import Optional,List
from pydantic import BaseModel
from datetime import date,datetime

from pydantic import constr

class PhotoCreate(BaseModel):
    owner_username :str
    house_id :int
    photo_no :int
    img_url :str
    
    class Config():  #to convert non dict obj to json
        orm_mode = True
    