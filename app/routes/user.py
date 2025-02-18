from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
#zaimportować schemas
from ..table.User import User
from ..table.Cart import Cart
from ..schemas import UserSchema
from ..services import UserService, CartService
from ..database import get_db
from email_validator import validate_email

router = APIRouter()

def check_email(mail):
    try:
        valid = validate_email(mail)
        return True
    except:
        return False

@router.post("/signin", response_model=UserSchema.UserResponse)
async def register(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    if len(user.username) == 0 or len(user.email) == 0 or len(user.password)==0:
        raise HTTPException(status_code=400, detail="Nie uzupełniono wszystkich pól.")
    
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Użytkownik o takiej nazwie lub e-mailu już istnieje.")

    

    if not check_email(user.email):
        raise HTTPException(status_code=400, detail="Nieprawidłowy adres Email.")

    user = UserService.create_user(db, user)
    return {
            "username": user.username,
            "email": user.email,
            "userID": user.userID,
    }

@router.post("/login")
async def login(email: str, password: str, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(
        (User.email == email)
    ).first()

    if not existing_user:
        raise HTTPException(status_code=400, detail="Nie znaleziono użytkownika")

    correctPassword = UserService.verify_password(password, existing_user.hashed_password)

    if correctPassword:
        return {
            "status": "Okej"
        }
    else:
        raise HTTPException(status_code=400, detail="Nieprawidłowe hasło")
    
@router.get("/{userid}/cart")
async def getCart(userid: int, db: Session = Depends(get_db)):
    #Sprawdzenie, czy dla użytkownika jest kosz, jeżeli nie to zwraca komunikat o jego tworzeniu
    existing_cart = db.query(Cart).filter(
        (Cart.userId == userid)
    ).first()
    if not existing_cart:
        raise HTTPException(status_code=400, detail="Najpierw utwórz koszyk")
    else:
        return {
            "cart": existing_cart
        }


@router.post("/{userid}/cart")
async def postCart(userID: int, db: Session = Depends(get_db)):
    #Sprawdzenie czy istnieje już koszyk
    existing_cart = db.query(Cart).filter(
        (Cart.userId == userID)
    ).first()
    if not existing_cart:
        CartService.createCart(db, userID)
    else:
        raise HTTPException(status_code=400, detail="Koszyk już istnieje")

    


@router.put("/{userid}/cart")
async def putCart():
    return {"message": "User created successfully"}
    