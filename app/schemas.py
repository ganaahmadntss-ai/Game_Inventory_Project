from pydantic import BaseModel, Field
from typing import Optional

class ItemCreate(BaseModel):
    name: str = Field(min_length=2)
    category: str = Field(min_length=2)
    quantity: int = Field(gt=0)

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = Field(default=None,gt=0)