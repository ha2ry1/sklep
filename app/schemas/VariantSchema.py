from pydantic import BaseModel

class VariantBase(BaseModel):
    productID: int
    imagePath: str
    color: str
    size: str
    quantity: int
    title: str
    price: float
    
class VariantCreate(VariantBase):
    pass

class VariantResponse(VariantBase):
    variantID: int
    class Config:
        from_attributes = True