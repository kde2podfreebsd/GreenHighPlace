from flask_migrate import Migrate
from app.config.config import app, db

from app.models.CustomerModel import Customer
from app.models.ProductModel import Product
from app.models.CartModel import Cart
from app.models.ActiveOrderModel import ActiveOrder
from app.models.CompleteOrderModel import CompleteOrder
from app.models.RefusalOrderModel import RefusalOrder
from app.models.AdminModel import Admin
from app.models.postModel import Post
from app.models.NewProductModel import Productnew


migrate = Migrate(app, db)

app.app_context().push()
