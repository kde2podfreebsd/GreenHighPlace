from app.config import db, app

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.BigInteger, nullable=False)
    nameOfProduct = db.Column(db.String, nullable=False)
    numOfProducts = db.Column(db.Integer, nullable=False)
    idFromProduct = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.nameOfProduct}#{self.numOfProducts}"

def addToCart(customer_id: int, nameOfProduct: str, numOfProducts: int, idFromProduct = int):
    try:
        with app.app_context():
            cart = Cart(customer_id=customer_id, nameOfProduct=nameOfProduct,
                        numOfProducts=numOfProducts, idFromProduct=idFromProduct)
            db.session.add(cart)
            db.session.commit()

            return 1
    except Exception as e:
        return print(e, "\naddToCart error")

def getCart(customer_id: int):
    try:
        with app.app_context():

            return Cart.query.filter_by(customer_id=customer_id).all()

    except Exception as e:
        return print(e, "\ngetCart error")

def getProductFromCart(id: int):
    try:
        with app.app_context():

            return Cart.query.filter_by(id=id).first()

    except Exception as e:
        return print(e, "\ngetProductFromCart error")

def changeNumOfProducts(id: int, numOfProducts: int):
    try:
        with app.app_context():
            product = Cart.query.filter_by(id=id).first()
            product.numOfProducts = numOfProducts
            db.session.commit()
    except Exception as e:
        return print(e, "\nchangeNumOfProducts error")
def getOfNumberOfProducts(customer_id: int):
    try:
        with app.app_context():

            return len(Cart.query.filter_by(customer_id=customer_id).all())

    except Exception as e:
        return print(e, "\ngetOfNumberOfProducts error")

def delProductFromCart(id: int):
    try:
        with app.app_context():
            product = Cart.query.filter_by(id=id).first()
            db.session.delete(product)
            db.session.commit()
    except Exception as e:
        return print(e, "\ndelProductFromCart error")
def delProductsFromCart(customer_id: int):
    try:
        with app.app_context():
            products = Cart.query.filter_by(customer_id=customer_id).all()
            for product in products:
                db.session.delete(product)
            db.session.commit()
    except Exception as e:
        return print(e, "\ndelProductsFromCart error")
