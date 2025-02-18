from sqlalchemy import Column, Integer, String
from ..database import Base

class Category(Base):
    __tablename__ = "Category"
    __table_args__ = {'extend_existing': True}

    categoryID = Column(Integer, primary_key=True, index=True)
    categoryName = Column(String, index=True)