from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    category: str = Field(min_length=1)
    quantity: int = Field(ge=0)