from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base  
from app.table.Product import Product
from app.table.Variant import Variant
from app.table.Department import Department
from app.table.Category import Category
import datetime

Base.metadata.create_all(bind=engine)  

# Zainicjuj sesję
db = SessionLocal()

def seed_data(db: Session):

    db.query(Product).delete()
    db.query(Variant).delete()
    db.query(Department).delete()
    db.query(Category).delete()
    db.commit()
    
    categories = [
        Category(categoryName='Basics'),
        Category(categoryName='Blazer'),
        Category(categoryName='Knitwear'),
        Category(categoryName='Jeans'),
        Category(categoryName='Jackets'),
        Category(categoryName='Girl'),
        Category(categoryName='Boy'),
    ]
    db.add_all(categories)
    db.commit()

    departments = [
        Department(name='Women', categories='Basics,Blazer'),
        Department(name='Men', categories='Knitwear,Jeans,Jackets'),
        Department(name='Kids', categories='Girl,Boy'),
    ]
    db.add_all(departments)
    db.commit()

    
    products = [
        Product(
            _id=1,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/7568/644/802/2/w/1920/7568644802_1_1_1.jpg?ts=1541152091085',
            title='Oversized Textured Top',
            description='High collar top with short cuffed sleeves. Asymmetric hem with side slits.',
            price=35.95,
            color='Gray',
            size='XS,S,M',
            quantity=10,
            department='Women',
            category='Basics',
            date=datetime.datetime.now()
        ),
        Product(
            _id=2,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/5644/641/800/2/w/1920/5644641800_2_5_1.jpg?ts=1540395699528',
            title='Tank Top',
            description='Flowy V-neck camisole with spaghetti straps.',
            price=29.99,
            color='Black',
            size='XS,S,XL',
            quantity=15,
            department='Women',
            category='Basics',
            date=datetime.datetime.now()
        ),
        Product(
            _id=3,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/7568/469/251/2/w/1920/7568469251_2_1_1.jpg?ts=1540393989160',
            title='Basic Top',
            description='Round neck long sleeved shirt.',
            price=25.99,
            color='White',
            size='XS',
            quantity=90,
            department='Women',
            category='Basics',
            date=datetime.datetime.now()
        ),
        Product(
            _id=4,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/8197/757/093/4/w/1920/8197757093_2_2_1.jpg?ts=1538393944729',
            title='Belted Plaid Blazer',
            description='Flowy blazer with lapel collar and long sleeves. Self belt. Chest patch pockets and welt pockets at hip. Front double-breasted button closure.',
            price=79.99,
            color='Black',
            size='S,M,L',
            quantity=4,
            department='Women',
            category='Blazer',
            date=datetime.datetime.now()
        ),
        Product(
            _id=5,
            imagePath='https://static.zara.net/photos///2018/I/0/2/p/1775/300/615/2/w/1920/1775300615_1_1_1.jpg?ts=1539690384503',
            title='Perl Knit Swear',
            description='Purl-stitch knit sweater in a combination of textures. Ribbed trim.',
            price=79.99,
            color='Orange',
            size='M,L',
            quantity=5,
            department='Men',
            category='Knitwear',
            date=datetime.datetime.now()
        ),
        Product(
            _id=6,
            imagePath='https://static.zara.net/photos///2018/I/0/2/p/6186/352/407/2/w/1920/6186352407_2_1_1.jpg?ts=1540990017618',
            title='Ripped Jeans',
            description='Slim fit jeans with five pockets, washed effect, and rips on the legs. Zippered hem at in-seams. Front zip and metal button closure.',
            price=79.99,
            color='Dark Blue',
            size='M,L',
            quantity=80,
            department='Men',
            category='Jeans',
            date=datetime.datetime.now()
        ),
        Product(
            _id=7,
            imagePath='https://static.zara.net/photos///2018/I/0/2/p/5575/380/406/2/c-158-0-2048-3072/w/1920/5575380406_1_1_1.jpg?ts=1527530663760',
            title='Basic Slim Jeans',
            description='Basic slim-fit jeans with five pockets. Two side pockets, two back pockets, and one coin pocket. Belt loops. Front hidden zipper and button closure.',
            price=45.99,
            color='Light Blue',
            size='XS,S,M',
            quantity=8,
            department='Men',
            category='Jeans',
            date=datetime.datetime.now()
        ),
        Product(
            _id=8,
            imagePath='https://static.zara.net/photos///2018/I/0/2/p/3548/350/700/2/c-192-0-2048-3072/w/1920/3548350700_2_1_1.jpg?ts=1528819649601',
            title='Faux Leather Perforated Jacket',
            description='Faux leather perforated jacket with high collar and long sleeves. Two front zip pockets. Lined. Interior pocket. Front zip closure. Ribbed elastic hem and cuffs.',
            price=99.99,
            color='Brown',
            size='XS,M,XL',
            quantity=12,
            department='Men',
            category='Jackets',
            date=datetime.datetime.now()
        ),
        Product(
            _id=9,
            imagePath='https://static.zara.net/photos///2020/I/0/3/p/0257/700/703/102/w/560/0257700703_2_10_1.jpg?ts=1596028794347',
            title='SWEATSHIRT WITH TEXT',
            description='Round neck sweatshirt with long sleeves. Front printed text.',
            price=16.99,
            color='OYSTER WHITE',
            size='XS,M',
            quantity=23,
            department='Kids',
            category='Girl',
            date=datetime.datetime.now()
        ),
        Product(
            _id=10,
            imagePath='https://static.zara.net/photos///2020/I/0/3/p/3183/700/800/2/w/560/3183700800_1_1_1.jpg?ts=1597336424462',
            title='PADDED BOMBER',
            description='Quilted bomber jacket with round neck and long sleeves. Front hidden zip and snap button closure. Front pockets.',
            price=45.99,
            color='BLACK',
            size='XS',
            quantity=23,
            department='Kids',
            category='Boy',
            date=datetime.datetime.now()
        ),
    ]
    db.add_all(products)
    db.commit()

    
    variants = [
        Variant(
            productID=1,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/7568/644/710/2/w/1920/7568644710_1_1_1.jpg?ts=1541151891840',
            color='Beige',
            size='S,L',
            quantity=5,
            price=35.95   
        ),
        Variant(
            productID=2,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/5644/641/735/2/w/1920/5644641735_2_5_1.jpg?ts=1540395590656',
            color='Copper',
            size='S,L,XL',
            quantity=12,
            price=29.99   
        ),
        Variant(
            productID=3,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/7568/469/605/2/w/1920/7568469605_2_1_1.jpg?ts=1540394095062',
            color='Maroon',
            size='XS,M,L',
            quantity=4,
            price=25.99   
        ),
        Variant(
            productID=4,
            imagePath='https://static.zara.net/photos///2018/I/0/1/p/7568/469/822/2/w/1920/7568469822_2_1_1.jpg?ts=1540394193241',
            color='Charcoal',
            size='XS,L,XL',
            quantity=5,
            price=79.99   
        ),
        Variant(
            productID=5,
            imagePath='https://static.zara.net/photos///2018/I/0/2/p/1775/300/806/2/w/1920/1775300806_2_1_1.jpg?ts=1539690394197',
            color='Stone',
            size='S,XL',
            quantity=35,
            price=79.99   
        ),
        Variant(
            productID=6,
            imagePath='https://static.zara.net/photos///2018/I/0/2/p/5575/380/407/2/c-269-0-2048-3072/w/1920/5575380407_1_1_1.jpg?ts=1527602989905',
            color='Dark Blue',
            size='M,XL',
            quantity=5,
            price=45.99   
        ),
        Variant(
            productID=9,
            imagePath='https://static.zara.net/photos///2020/I/0/3/p/0257/700/800/102/w/560/0257700800_2_10_1.jpg?ts=1596028794110',
            color='BLACK',
            size='M,XL',
            quantity=5,
            price=16.90   
        )
    ]

    db.add_all(variants)
    db.commit()

if __name__ == "__main__":
    seed_data(db)
