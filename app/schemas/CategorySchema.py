from pydantic import BaseModel

class CategoryBase(BaseModel):
    categoryName: str
    
class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    categoryID: int
    class Config:
        from_attributes = True