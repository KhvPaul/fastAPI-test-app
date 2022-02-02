from typing import List

from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class BlogEdit(BlogBase):
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class ShowOnlyUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowOnlyUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
