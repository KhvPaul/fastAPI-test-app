from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import database, schemas, oauth2
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['User'],
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.UserBase, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db),
             current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return user.get_user(id, db)
