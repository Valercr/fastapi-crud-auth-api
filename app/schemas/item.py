from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str | None = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str | None

    class Config:
        from_attributes = True # de SQLAlchemy a Pydantic (de bd a id, name, description)