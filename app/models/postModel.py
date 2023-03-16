from app.config import db, app

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    chatId = db.Column(db.BigInteger, nullable=False)
    textRU = db.Column(db.String, nullable=True)
    textEN = db.Column(db.String, nullable=True)
    dirMedia = db.Column(db.String, nullable=True)
    dirType = db.Column(db.String, nullable=True)
    def __repr__(self):
        return f'{self.id}-#-#-{self.chatId}-#-#-{self.textRU}-#-#-{self.textEN}-#-#-{self.dirMedia}-#-#-{self.dirType}'
def addToPost(chatId: int):
    try:
        with app.app_context():
            cart = Post(chatId=chatId)
            db.session.add(cart)
            db.session.commit()

            return 1
    except Exception as e:
        return print(e, "\naddToPost error")

def setTextRU(chatId, textRU):
    try:
        with app.app_context():
            if Post.query.filter_by(chatId=chatId).first():
                customer = Post.query.filter_by(chatId=chatId).first()
                customer.textRU = textRU
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetTextRU error")

def setTextEN(chatId, textEN):
    try:
        with app.app_context():
            if Post.query.filter_by(chatId=chatId).first():
                customer = Post.query.filter_by(chatId=chatId).first()
                customer.textEN = textEN
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetTextEN error")
def setDirType(chatId, type):
    try:
        with app.app_context():
            if Post.query.filter_by(chatId=chatId).first():
                customer = Post.query.filter_by(chatId=chatId).first()
                customer.dirType = type
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetTextRU error")

def setDirMedia(chatId, dir):
    try:
        with app.app_context():
            if Post.query.filter_by(chatId=chatId).first():
                customer = Post.query.filter_by(chatId=chatId).first()
                customer.dirMedia = dir
                db.session.commit()
                return 1
            else:
                return 0

    except Exception as e:
        return print(e, "\nsetTextRU error")

def getPost(chatId: int):
    try:
        with app.app_context():
            return Post.query.filter_by(chatId=chatId).first()

    except Exception as e:
        return print(e, "\ngetPost error")

def delPost(chatId: int):
    try:
        with app.app_context():
            post = Post.query.filter_by(chatId=chatId).first()
            db.session.delete(post)
            db.session.commit()
    except Exception as e:
        return print(e, "\ndelPost error")