from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
#from ..models.Product import Product
from ..table.Product import Product
from ..table.Variant import Variant
from ..table.Department import Department
from ..table.Category import Category
from ..services import ProductService
from ..database import get_db

router = APIRouter()

@router.get("/products")
async def getProducts(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    if len(products)<1:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktów")
    return {"products": products}
    
@router.get("/products/{productID}")
async def getProductsById(productID: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(
        (Product.productID == productID)
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu")
    return {"product": product}
    
@router.get("/variants")
async def getVariants(db: Session = Depends(get_db)):
    variants = db.query(Variant).all()
    if len(variants)<1:
        raise HTTPException(status_code=404, detail="Nie znaleziono wariantów")
    return {"variants": variants}
    
@router.get("/variants/{variantID}")
async def getVariantsById(variantID: int, db: Session = Depends(get_db)):
    variant = db.query(Product).filter(
        (Variant.variantID == variantID)
    ).first()
    if not variant:
        raise HTTPException(status_code=404, detail="Nie znaleziono wariantu")
    return {"variant": variant}
    
@router.get("/departments")
async def getDepartments(db: Session = Depends(get_db)):
    departments = db.query(Department).all()
    if len(departments)<1:
        raise HTTPException(status_code=404, detail="Nie znaleziono działów")
    return {"departments": departments}
    
@router.get("/categories")
async def getDepartments(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    if len(categories)<1:
        raise HTTPException(status_code=404, detail="Nie znaleziono kategorii")
    return {"categories": categories}
    
@router.get("/search")
async def getSearch(query: dict, db: Session = Depends(get_db)):
    query['department'] = query['query']
    products = ProductService.getProductByDepartment(query)
    if len(products)>0:
        return {"products": products}
    else:
        query['category'] = query['department']
        products = ProductService.getProductByCategory(query)
        if len(products)>0:
            return {"products": products}
        else:
            query['title'] = query['category']
            products = ProductService.getProductByTitle(query)
            if len(products)>0:
                return {"products": products}
            else:
                query['id'] = query['title']
                products = ProductService.getProductById(query)
                if len(products)>0:
                    return {"products": products}
                else:
                    raise HTTPException(status_code=404, detail="Nie znaleziono produktu")

    
@router.get("/filter")
async def getFilter(db: Session = Depends(get_db)):
    result = {}
    p = ProductService.filterProductByDepartment()
    if len(p)>0:
        result['department'] = p
    p = ProductService.filterProductByCategory()
    if len(p)>0:
        result['category'] = p
    p = ProductService.filterProductByTitle()
    if len(p)>0:
        result['title'] = p
    if len(result.keys) > 0:
        return {"filter": result}
    else:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu")

    
@router.get("/checkout")
async def getCheckout():
    pass #Zaślepka w zależności jaki rodzaj płatności (w oryginale był PayPal)
    
@router.get("/payment/success")
async def getPaymentSuccess(paymentID: int, payerID: int):
    pass #Zaślepka w zależności jaki rodzaj płatności (w oryginale był PayPal)