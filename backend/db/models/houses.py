from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey,REAL
from sqlalchemy.orm import relationship
from typing import List
from db.base_class import Base
from sqlalchemy import LargeBinary
from sqlalchemy.types import Float




class House(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    rent = Column(Integer,nullable = False)
    no_rooms = Column(Integer,nullable = False)
    size = Column(Integer,nullable = False)
    additional_cost = Column(Integer,nullable = False)
    total_rent = Column(Integer,nullable = False)
    max_flatmates = Column(Integer,nullable = False)
    exist_fmates = Column(Integer,nullable = False)
    heating_type = Column(String,nullable= False)
    heating_cost = Column(Integer,nullable = False)
    city = Column(String,nullable = False) 
    adress = Column(String,nullable = False)
    zipcode = Column(Integer,nullable = False)
    description = Column(String,nullable=False)
    min_duration = Column(Integer,nullable = False)
    smoking_allowed = Column(Boolean,nullable = False)
    parking = Column(String,nullable = False)
    postedby = Column(String,nullable = False)
    date_posted = Column(Date)
    img_url = Column(String,nullable = True)
    img_url2 = Column(String,nullable = True)
    lat= Column(Float,nullable=True)
    lng= Column(Float,nullable=True)
    is_active = Column(Boolean(),default=True)
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("User",back_populates="houses")
    
