from typing import List, Optional
from fastapi import Request


class UserCreateForm:
    def __init__(self,request:Request):
        self.request: Request = request
        self.errors : List = []
        self.username : Optional[str] = None
        self.email : Optional[str]= None
        self.password : Optional[str]= None
        self.max_rent : Optional[int] = None
        self.smoking  : Optional[bool] = None
        self.religion : Optional[str] = None
        self.profession :Optional[str] = None
        self.want_fmates : Optional[bool] = None
        self.hobbies : Optional[str] = None
        self.languages : Optional[str] = None
        self.role :Optional[str] = None
        self.is_active : Optional[bool] = None
        self.is_superuser : Optional[bool] = None
        

    async def load_data(self):
            form = await self.request.form()
            self.username= form.get("username")
            self.email= form.get("email")
            self.password = form.get("password")
            self.max_rent = form.get("max_rent")
            self.smoking = form.get("smoking")
            self.religion = form.get("religion")
            self.profession = form.get("profession")
            self.want_fmates = form.get("want_fmates")
            self.hobbies = form.get("hobbies")
            self.languages = form.get("languages")
            self.role = form.get("role")
            self.is_active = form.get("is_active")
            self.is_superuser = form.get("is_superuser")

    async def is_valid(self):
         if not self.username or not len(self.username) > 3:
              self.errors.append("Username should be more than 3 characters!")
         #if not self.email or not len(self.email.__contains__("@")):
          #    self.errors.append("Email is required!")
         if not self.password or not len(self.password) >= 4:
              self.errors.append("Password should be more than 4 characters!")
         if not self.errors:
              return True
         return False

            
         
