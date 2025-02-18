from sqlalchemy import Column, Integer, String
from database import Base

class Department(Base):
    __tablename__ = "Department"
    __table_args__ = {'extend_existing': True}
    
    departmentID = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    categories = Column(Integer)