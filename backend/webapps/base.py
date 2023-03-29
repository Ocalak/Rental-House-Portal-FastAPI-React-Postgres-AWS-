from fastapi import APIRouter
from webapps.houses import route_houses
from webapps.users import route_users  #new
from webapps.auth import route_login   #new 


api_router = APIRouter()
api_router.include_router(route_houses.router, prefix="", tags=["house-webapp"])
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])   #new
