from app.database import Base, engine
from app.table import User, Cart, Category, Department, Product, Variant

Base.metadata.create_all(bind=engine)