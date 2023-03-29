from typing import Optional
from pydantic import BaseModel,EmailStr
from enum import Enum



#properties required during user creation
class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str
    max_rent : int
    smoking : bool
    religion : str
    profession : str
    want_fmates : bool
    hobbies : str
    languages : str
    role : str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    username: str
    email : EmailStr
    is_active : bool
    max_rent : int
    smoking : bool
    religion : str
    profession : str
    want_fmates : bool
    hobbies : str
    languages : str
    role : str

    class Config():
        orm_mode = True




