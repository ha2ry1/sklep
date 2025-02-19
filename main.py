import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import user, index
from app.models import User, Cart, Category, Department, Product, Variant

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Dodatnie routów, czyli endpointów połączeniowych przez https://strona/ENDPOINT
app.include_router(user.router, prefix="/user", tags=["Authentication"])
app.include_router(index.router, prefix="", tags=["Products"])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)