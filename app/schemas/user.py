from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True # de SQLAlchemy a PydantiC


class UserLogin(BaseModel):
    username: str
    password: str
    