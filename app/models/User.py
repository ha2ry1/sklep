from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = "User"
    __table_args__ = {'extend_existing': True}
    
    userID = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)