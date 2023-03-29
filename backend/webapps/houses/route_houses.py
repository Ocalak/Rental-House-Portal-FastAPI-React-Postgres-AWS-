from fastapi import APIRouter
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.repository.houses import list_houses
from db.session import get_db
from db.repository.houses import retreive_house  
from db.models.users import User  
from apis.version1.route_login import get_current_user_from_token
from webapps.houses.forms import HouseCreateForm
from schemas.houses import HouseCreate
from db.repository.houses import create_new_house
from fastapi import responses, status
from fastapi.security.utils import get_authorization_scheme_param




templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/houses")
async def home(request: Request,db: Session = Depends(get_db)):
    houses = list_houses(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request,"houses":houses}
    )
@router.get("/details/{id}")             #new
def house_detail(id:int,request: Request,db:Session = Depends(get_db)):    
    house = retreive_house(id=id, db=db)
    return templates.TemplateResponse(
        "houses/detail.html", {"request": request,"house":house}
    )


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db),msg:str = None):   #new
    #houses = list_houses(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "msg":msg}   #new
    )
#@router.get("/register/")
#def register(request: Request):
    #return templates.TemplateResponse("users/register.html", {"request": request})


@router.get("/post-a-house/")       #new 
def create_house(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("houses/create_house.html", {"request": request})


@router.post("/post-a-house/")    #new
async def create_house(request: Request,db: Session = Depends(get_db)):
    form = HouseCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            house = HouseCreate(**form.__dict__)
            house = create_new_house(house=house, db=db 
                                     ,owner_id=current_user.id
                                     )
            return responses.RedirectResponse(
                f"/details/{house.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("houses/create_house.html", form.__dict__)
    return templates.TemplateResponse("houses/create_house.html", form.__dict__)

'''@router.post("/create-house/",response_model=ShowHouse)
def create_house(house: HouseCreate,db: Session = Depends(get_db)):
    current_user = 1
    house = create_new_house(house=house,db=db,owner_id=current_user)
    return(house)'''