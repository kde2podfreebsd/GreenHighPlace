from app.config import db, app

from app.models import NewProductModel as npm
class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    typeMedia = db.Column(db.String, nullable=True)
    dirMedia = db.Column(db.String, nullable=True)
    infoAbout = db.Column(db.String, nullable=True)
    queue = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"{self.id}-#-#-{self.name}-#-#-{self.price}-#-#-{self.dirMedia}-#-#-{self.infoAbout}"

# /home/fake_svoevolin/Desktop/tgBot_BOSHKI_PHUKET/Media/1.png

def addProduct(name: str, price: int):
    try:
        with app.app_context():
            lastNumber = Product.query.filter(Product.id is not None).all()[-1].queue

            product = Product(name=name, price=price, queue=lastNumber + 1)
            db.session.add(product)
            db.session.commit()
            c = Product.query.filter(Product.id is not None).all()

            return c[-1].id

    except Exception as e:
        return print(e, "\nProduct error")


def addProductStart(name: str, price: int):
    try:
        with app.app_context():
            lastNumber = Product.query.filter(Product.id is not None).all()[-1].queue

            product = Product(name=name, price=price, queue=lastNumber + 1)
            db.session.add(product)
            db.session.commit()
            c = Product.query.filter(Product.id is not None).all()

            return c[-1].id

    except Exception as e:
        return print(e, "\nProduct error")
def setType(id, type):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                customer = Product.query.filter_by(id=id).first()
                customer.typeMedia = type
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetTextRU error")

def setName(id, name):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                product.name = name
                db.session.commit()
                return {"message": f'dirMedia set is {product.dirMedia}', "status": True}
            else:
                return {"message": 'No product with this name', "status": False}

    except Exception as e:
        return print(e, "\nsetLanguage error")

def setPrice(id, price):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                product.price = price
                db.session.commit()
                return {"message": f'dirMedia set is {product.dirMedia}', "status": True}
            else:
                return {"message": 'No product with this name', "status": False}

    except Exception as e:
        return print(e, "\nsetLanguage error")
def setMedia(id, file_path):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                product.dirMedia = file_path
                db.session.commit()
                return {"message": f'dirMedia set is {product.dirMedia}', "status": True}
            else:
                return {"message": 'No product with this name', "status": False}

    except Exception as e:
        return print(e, "\nsetLanguage error")
def getMedia(id):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                customer = Product.query.filter_by(id=id).first()
                # print(customer.dirMedia)
                return customer.dirMedia
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\ngetLanguage error")

def getPrice(id):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                return product.price
            else:
                return False

    except Exception as e:
        return print(e, "\ngetPrice error")
def setInfoAbout(id, info):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                product.infoAbout = info
                db.session.commit()
                return {"message": f'InfoAbout set is {product.infoAbout}', "status": True}
            else:
                return {"message": 'No product with this name', "status": False}

    except Exception as e:
        return print(e, "\nsetLanguage error")

def changeInfoAboutRU(id, infoAbout):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                newprod = Product.query.filter_by(id=id).first()
                newprod.infoAbout = infoAbout + "#" + newprod.infoAbout.split("#")[1]
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetInfoAboutRU error")

def changeInfoAboutEN(id, infoAbout):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                newprod = Product.query.filter_by(id=id).first()
                newprod.infoAbout = newprod.infoAbout.split("#")[0] + "#" + infoAbout
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetInfoAboutEN error")

def getName(id):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                return product.name
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\ngetLanguage error")
def getInfoAbout(id):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                product = Product.query.filter_by(id=id).first()
                return product.infoAbout
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\ngetLanguage error")

def getProduct(id: int):
    try:
        with app.app_context():

            return Product.query.filter_by(id=id).first()


    except Exception as e:
        return print(e, "\ngetProduct error")
def getProducts():
    try:
        with app.app_context():

            allProducts = Product.query.filter(Product.id != None).all()
            dictOfQueue = {}

            for one in allProducts:
                dictOfQueue[one.queue] = one

            listOfQueue = sorted(dictOfQueue)
            finalList = list()
            for i in listOfQueue:
                finalList.append(dictOfQueue[i])
            return finalList
    except Exception as e:
        return print(e, "\ngetProduct error")

def countMedia(id):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                newprod = Product.query.filter_by(id=id).first()
                return len(list(newprod.dirMedia.split('#'))) // 2
            else:
                return Exception

    except Exception as e:
        return print(e, "\nsetDirMedia error")

def delProduct(id: int):
    try:
        with app.app_context():
            product = Product.query.filter_by(id=id).first()
            db.session.delete(product)
            db.session.commit()
    except Exception as e:
        return print(e, "\ndelProduct error")

def setDirMedia(id, dirMedia):
    try:
        with app.app_context():
            if Product.query.filter_by(id=id).first():
                newprod = Product.query.filter_by(id=id).first()
                newprod.dirMedia = dirMedia
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetDirMedia error")

def switcherNewProductToStartProduct(newprod: npm.Productnew):
    try:
        with app.app_context():

            allProducts = getProducts()

            for everyone in allProducts:
                everyone.queue += 1


            product = Product(
                name=newprod.name,
                price=newprod.price,
                typeMedia=newprod.typeMedia,
                dirMedia=newprod.dirMedia,
                infoAbout=newprod.infoAbout,
                queue=1
            )

            db.session.delete(newprod)
            db.session.add(product)
            db.session.add_all(allProducts)
            db.session.commit()
            return 1

    except Exception as e:
        return print(e, "\nswitcherNewProductToProduct error")

def switcherNewProductToFinishProduct(newprod: npm.Productnew):
    try:
        with app.app_context():

            lastNumber = 0
            allProducts = getProducts()
            if len(allProducts) != 0:
                for one in allProducts:
                    if one.queue > lastNumber:
                        lastNumber = one.queue


            product = Product(
                name=newprod.name,
                price=newprod.price,
                typeMedia=newprod.typeMedia,
                dirMedia=newprod.dirMedia,
                infoAbout=newprod.infoAbout,
                queue=lastNumber + 1
            )

            db.session.delete(newprod)
            db.session.add(product)
            db.session.commit()
            return 1

    except Exception as e:
        return print(e, "\nswitcherNewProductToProduct error")