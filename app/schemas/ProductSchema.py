from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    imagePath: str
    title: str
    description: str
    department: int
    category: int
    price: float
    color: str
    size: str
    quantity: int
    date: datetime 
    
class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    productID: int
    class Config:
        from_attributes = True