from pydantic import BaseModel
from datetime import datetime

class DepartmentBase(BaseModel):
    name: str
    categories: int
    
class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    departmentID: int
    class Config:
        from_attributes = True