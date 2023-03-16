from app.config import db, app
from app.models import CartModel as cart
from datetime import datetime
from app.models import ProductModel as pm
import pytz

class ActiveOrder(db.Model):
    __tablename__ = 'active'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.BigInteger, nullable=False)
    items = db.Column(db.String, nullable=False)
    fullprice = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.String(64), nullable=False)
    methodpay = db.Column(db.String(64), nullable=True)
    status = db.Column(db.String(64), default="ожидает курьера")
    address = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"{self.id}-#-#-{self.customer_id}-#-#-{self.items}-#-#-{self.fullprice}-#-#-{self.datetime}" \
               f"-#-#-{self.methodpay}-#-#-{self.status}-#-#-{self.address}-#-#-{self.comment}"

def addActiveOrder(customer_id: int, fullprice: int, methodpay: str, address: str, comment: str):
    try:
        with app.app_context():
            products = cart.getCart(customer_id=customer_id)
            items = ""
            for product in products:
                # product = str(product)
                # name = product.split('#')[0]
                items += product.nameOfProduct + "#" + str(product.numOfProducts) + \
                         "#" + str(pm.getPrice(product.idFromProduct)) + ","

            dayandtime = str(datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%d/%m/%Y %H:%M"))
            if methodpay == "forCash":

                order = ActiveOrder(customer_id=customer_id,
                                    items=items,
                                    fullprice=fullprice,
                                    datetime=dayandtime,
                                    methodpay="наличные",
                                    address=address,
                                    comment=comment)

                # numberOfOrder = order.id
                cart.delProductsFromCart(customer_id)

                db.session.add(order)

                db.session.commit()
                c = ActiveOrder.query.filter(ActiveOrder.id is not None).all()

                return c[-1].id
    except Exception as e:
        return print(e, "\naddActiveOrder error")

def getActiveOrders(customer_id: int):
    try:
        with app.app_context():

            return ActiveOrder.query.filter_by(customer_id=customer_id).all()

    except Exception as e:
        return print(e, "\ngetActiveOrders error")

def switchStatus(id: int, time=""):
    try:
        with app.app_context():
            active = ActiveOrder.query.filter_by(id=id).first()
            active.status = "Передано на доставку" + "#" + time
            db.session.add(active)
            db.session.commit()
            return 1

    except Exception as e:
        return print(e, "\nswitchStatus error")

def getAllActiveOrders():
    try:
        with app.app_context():

            return ActiveOrder.query.filter(ActiveOrder.id is not None).all()

    except Exception as e:
        return print(e, "\ngetAllActiveOrders error")
def getActiveOrder(id: int):
    try:
        with app.app_context():

            return ActiveOrder.query.filter_by(id=id).first()

    except Exception as e:
        return print(e, "\ngetActiveOrder error")
def delFromActive(id: int):
    try:
        with app.app_context():
            active = ActiveOrder.query.filter_by(id=id).first()
            db.session.delete(active)
            db.session.commit()
    except Exception as e:
        return print(e, "\ndelFromActive error")
