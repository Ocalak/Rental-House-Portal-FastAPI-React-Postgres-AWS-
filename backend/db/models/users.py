from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Enum
from sqlalchemy.orm import relationship

from db.base_class import Base



class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    role = Column(String,nullable=False)
    max_rent = Column(Integer,nullable=False)
    smoking = Column(Boolean,nullable=False)
    religion = Column(String,nullable=True)
    profession = Column(String,nullable=False)
    want_fmates = Column(Boolean,nullable=False)
    hobbies = Column(String,nullable = False)
    languages = Column(String,nullable = False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)
    houses = relationship("House",back_populates="owner")
