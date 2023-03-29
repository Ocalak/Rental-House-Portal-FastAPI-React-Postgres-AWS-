import pgeocode
from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from fastapi.encoders import jsonable_encoder

import requests
api_key = "x"
countrycode = "DE"
zip_code= 47226
adress="Bertastrasse 19"

#url = f"https://thezipcodes.com/api/v1/search?zipCode={zip_code}&countryCode={countrycode}&apiKey={api_key}"

#response = requests.get(url)
#json_data = response.json()
#print(json_data['location'][0]['longitude'],json_data['location'][0]['latitude'])

def geozip(countrycode:str,zipcode:int):
    url = f"https://thezipcodes.com/api/v1/search?zipCode={zip_code}&countryCode={countrycode}&apiKey={api_key}"
    response = requests.get(url)
    json_data = response.json()
    
    return(json_data['location'][0]['longitude'],json_data['location'][0]['latitude'])
aa = geozip(countrycode,zip_code)
bb = float(aa[0])
print(bb)
