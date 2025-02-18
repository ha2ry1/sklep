from sqlalchemy.orm import Session
from models.Cart import Cart

def createCart(db: Session, userID: int):
    db_cart = Cart(items = "", totalQty=0, totalPrice=0, userId=userID)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart