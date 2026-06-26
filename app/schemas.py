from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    category: str
    quantity: int