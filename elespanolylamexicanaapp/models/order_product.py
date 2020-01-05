from django.db import models
from elespanolylamexicanaapp.models.product import Product
from elespanolylamexicanaapp.models.order import Order

class OrderProduct( models.Model ):
    order = models.ForeignKey( Order, on_delete=True )
    product = models.ForeignKey( Product, on_delete = True )