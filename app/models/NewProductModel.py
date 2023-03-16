from app.config import db, app


class Productnew(db.Model):
    __tablename__ = 'newproduct'

    id = db.Column(db.Integer, primary_key=True)
    chatId = db.Column(db.BigInteger, nullable=True)
    name = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    typeMedia = db.Column(db.String, nullable=True)
    dirMedia = db.Column(db.String, nullable=True, default="")
    infoAbout = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"{self.id}-#-#-{self.name}-#-#-{self.price}-#-#-{self.dirMedia}-#-#-{self.infoAbout}"

def addNewProduct(chatId: int):
    try:
        with app.app_context():
            newprod = Productnew(chatId=chatId)
            db.session.add(newprod)
            db.session.commit()

            return 1
    except Exception as e:
        return print(e, "\naddNewProduct error")

def setName(chatId, name):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.name = name
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetName error")

def setInfoAboutRU(chatId, infoAbout):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.infoAbout = infoAbout
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetInfoAboutRU error")

def setInfoAboutEN(chatId, infoAbout):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.infoAbout = newprod.infoAbout + "#" + infoAbout
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetInfoAboutEN error")

def setPrice(chatId, price):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.price = price
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetInfoAbout error")

def setType(chatId, type):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.typeMedia = type
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetType error")

def setDirMedia(chatId, dirMedia):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.dirMedia = dirMedia
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetDirMedia error")

def addDirMedia(chatId, dirMedia):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                newprod.dirMedia += dirMedia
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetDirMedia error")

def countMedia(chatId):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                return len(list(newprod.dirMedia.split('#'))) // 2
            else:
                return Exception

    except Exception as e:
        return print(e, "\nsetDirMedia error")

def getMedias(chatId):
    try:
        with app.app_context():
            if Productnew.query.filter_by(chatId=chatId).first():
                newprod = Productnew.query.filter_by(chatId=chatId).first()
                print(newprod.dirMedia)
                medias = list()
                # 1 2 3 4 5 6 7 8, 1 3 5 7 9 11 13 15
                for i in range(len(list(newprod.dirMedia.split('#'))) // 2):
                    medias.append(newprod.dirMedia.split('#')[2 * (i + 1) - 1])
                print(medias)
                return medias
            else:
                return Exception

    except Exception as e:
        return print(e, "\nsetDirMedia error")
def getNewProd(chatId: int):
    try:
        with app.app_context():
            return Productnew.query.filter_by(chatId=chatId).first()

    except Exception as e:
        return print(e, "\ngetPost error")
def delNewProd(chatId: int):
    try:
        with app.app_context():
            newprod = Productnew.query.filter_by(chatId=chatId).first()
            db.session.delete(newprod)
            db.session.commit()
    except Exception as e:
        return print(e, "\ndelNewProd error")

