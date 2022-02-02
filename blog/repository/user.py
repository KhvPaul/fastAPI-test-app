from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import schemas, models
from blog.hashing import Hash


def get_user(id: int, db: Session):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()      ALT
    user = db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'detail': f'User with id {id} not available'})
    return user


def create(request: schemas.UserBase, db: Session):
    request.password = Hash.bcrypt(request.password)
    new_user = models.User(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
