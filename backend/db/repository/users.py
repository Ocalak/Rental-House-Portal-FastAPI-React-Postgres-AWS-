from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user:UserCreate,db:Session):
    user = User(username=user.username,
        email = user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        max_rent = user.max_rent,
        smoking = user.smoking,
        religion = user.religion,
        profession = user.profession,
        want_fmates = user.want_fmates,
        hobbies = user.hobbies,
        languages = user.languages,
        role = user.role,
        is_active=True,
        is_superuser=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 


def list_users(db: Session):
    users = db.query(User).all()
    return users


async def get_user_by_email(email: str, db:Session):
    return db.query(User).filter(User.email ==  email).first()
