from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Cart(Base):
    __tablename__ = "Cart"
    __table_args__ = {'extend_existing': True}
    
    cartID = Column(Integer, primary_key=True, index=True)
    items = Column(String, index=True)
    totalQty = Column(Integer)
    totalPrice = Column(Float)
    userId = Column(Integer)