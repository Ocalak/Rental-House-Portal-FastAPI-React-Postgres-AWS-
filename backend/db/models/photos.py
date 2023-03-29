from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from typing import List

from db.base_class import Base



class Photo(Base):
    id = Column(Integer, primary_key=True, index=True)
    owner_username = Column(String,nullable=False)
    house_id = Column(Integer,nullable=False)
    photo_no = Column(Integer,nullable=False)
    img_url = Column(String,nullable= False)