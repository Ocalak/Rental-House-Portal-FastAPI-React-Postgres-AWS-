from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from db.session import engine   #new
from db.base import Base  #ne
from apis.base import api_router #new
from pydantic import validate_email

#/Users/ocalkaptan/Desktop/fastx/env

def include_router(app):
	app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():           #new
	print("create_tables")
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()       #new
	return app

app = start_application()
