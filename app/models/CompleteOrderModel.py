from app.config import db, app
from datetime import datetime
from app.models import ActiveOrderModel as ao
import pytz



class CompleteOrder(db.Model):
    __tablename__ = 'complete'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.BigInteger, nullable=False)
    items = db.Column(db.String, nullable=False)
    fullprice = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.String(64), nullable=False)
    methodpay = db.Column(db.String(64), nullable=True)
    datetime_complete = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=True)
    id_from_active = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"{self.id}-#-#-{self.customer_id}-#-#-{self.items}" \
               f"-#-#-{self.fullprice}-#-#-{self.datetime}-#-#-{self.methodpay}-#-#-{self.datetime_complete}" \
               f"-#-#-{self.address}-#-#-{self.comment}-#-#-{self.id_from_active}"


def getAllCompleteOrders():
    try:
        with app.app_context():

            return CompleteOrder.query.filter(CompleteOrder.id is not None).all()

    except Exception as e:
        return print(e, "\ngetAllCompleteOrders error")
def getCompleteOrder(customer_id: int):
    try:
        with app.app_context():

            return CompleteOrder.query.filter_by(customer_id=customer_id).all()

    except Exception as e:
        return print(e, "\ngetCompleteOrder error")

def getCompleteOrders(customer_id: int):
    try:
        with app.app_context():

            return CompleteOrder.query.filter_by(customer_id=customer_id).all()

    except Exception as e:
        return print(e, "\ngetCompleteOrders error")

def switcherActiveToComplete(active: ao.ActiveOrder):
    try:
        with app.app_context():
            complete = CompleteOrder(
                customer_id=active.customer_id,
                items=active.items,
                fullprice=active.fullprice,
                datetime=active.datetime,
                methodpay=active.methodpay,
                datetime_complete=str(datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%d/%m/%Y %H:%M")),
                address=active.address,
                comment=active.comment,
                id_from_active=active.id
            )

            db.session.delete(active)
            db.session.add(complete)
            db.session.commit()
            return 1

    except Exception as e:
        return print(e, "\nswitcherActiveToComplete error")

