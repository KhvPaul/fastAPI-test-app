from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..repository import blog
from blog import database, schemas, oauth2

router = APIRouter(
    prefix='/blog',
    tags=['Blog'],
)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db),
            current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(database.get_db),
             current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.get_blog(id, db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogEdit, db: Session = Depends(database.get_db),
           current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, request: schemas.BlogEdit, db: Session = Depends(database.get_db),
           current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db),
           current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)
