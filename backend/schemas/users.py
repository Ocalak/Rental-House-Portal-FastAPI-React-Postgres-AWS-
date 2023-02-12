from typing import Optional
from pydantic import BaseModel


#properties required during user creation
class UserCreate(BaseModel):
    username: str
    email : str
    password : str