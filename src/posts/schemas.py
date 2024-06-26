from pydantic import BaseModel, EmailStr, constr

class PostBase(BaseModel):
    text: constr(max_length=1000)

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
