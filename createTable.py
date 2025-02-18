from app.database import Base, engine
from table import User, Cart, Category, Department, Product, Variant

Base.metadata.create_all(bind=engine)