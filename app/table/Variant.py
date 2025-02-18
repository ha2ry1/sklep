from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Variant(Base):
    __tablename__ = "Variant"
    __table_args__ = {'extend_existing': True}
    
    variantID = Column(Integer, primary_key=True, index=True)
    productID = Column(Integer)
    imagePath = Column(String)
    color = Column(String)
    size = Column(String)
    quantity = Column(Integer)
    title = Column(String)
    price = Column(Float)