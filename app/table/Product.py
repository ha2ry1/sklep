from sqlalchemy import Column, Integer, String, Float, Date
from ..database import Base

class Product(Base):
    __tablename__ = "Product"
    __table_args__ = {'extend_existing': True}
    
    productID = Column(Integer, primary_key=True, index=True)
    imagePath = Column(String)
    title = Column(String)
    description = Column(String)
    department = Column(Integer)
    category = Column(Integer)
    price = Column(Float)
    color = Column(String)
    size = Column(String)
    quantity = Column(Integer)
    date = Column(Date)