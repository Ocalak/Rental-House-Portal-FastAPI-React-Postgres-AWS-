from typing import List
from typing import Optional
from datetime import date,datetime
from fastapi import Request


class HouseCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.rent: Optional[int] = None
        self.no_rooms: Optional[int] = None
        self.size: Optional[int] = None
        self.additional_cost: Optional[int] = None
        self.total_rent: Optional[int] = None
        self.max_flatmates: Optional[int] = None
        self.exist_fmates: Optional[int] = None
        self.heating_type : Optional[str] = None
        self.heating_cost: Optional[int] = None
        self.city : Optional[str] = None
        self.adress: Optional[str] = None
        self.zipcode: Optional[int] = None
        self.description: Optional[str] = None
        self.min_duration: Optional[int] = None
        self.smoking_allowed : Optional[bool] = None
        self.parking: Optional[str] = None
        self.postedby: Optional[str] = None
        self.is_active : Optional[bool] = None
        self.data_posted : Optional[date] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.rent= form.get("rent")
        self.no_rooms= form.get("no_rooms")
        self.size= form.get("size")
        self.additional_cost= form.get("additional_cost")
        self.total_rent= form.get("total_rent")
        self.max_flatmates= form.get("max_flatmates")
        self.exist_fmates= form.get("exist_fmates")
        self.heating_type = form.get("heating_type")
        self.heating_cost= form.get("heating_cost")
        self.city = form.get("city")
        self.adress= form.get("adress")
        self.zipcode= form.get("zipcode")
        self.description= form.get("description")
        self.min_duration= form.get("min_duration")
        self.smoking_allowed = form.get("smoking_allowed")
        self.parking= form.get("parking")
        self.postedby= form.get("postedby")
        self.is_active = form.get("is_active")
        self.data_posted = form.get("date_posted")

    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("A valid title is required")
        if not self.rent or not int(self.rent) >= 0:
            self.errors.append("Rent must be bigger than 0 and number")
        if not self.size or not int(self.size) >= 0:
            self.errors.append("Size Must be number and bigger than zero")
        if not self.zipcode or not int(self.zipcode) >= 0:
            self.errors.append("Zipcode must be a number!")
        if not self.description or not len(self.description) >= 20:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False