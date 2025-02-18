from pydantic import BaseModel

class CartBase(BaseModel):
    items: str
    totalQty: int
    totalPrice: float
    userId: int
    
class CartCreate(CartBase):
    pass

class CartResponse(CartBase):
    cartID: int
    class Config:
        from_attributes = True