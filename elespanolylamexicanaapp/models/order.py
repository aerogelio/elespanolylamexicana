from django.db import models
from elespanolylamexicanaapp.models.product import Product
from elespanolylamexicanaapp.models.user_app import Userapp

class Order(models.Model):
    
    CANCEL = 'CANCELADA'
    PENDING = 'PENDIENTE'
    ACCEPTED = 'ACEPTADA'
    PREPARING = 'PREPARANDOSE'
    PICK_UP = 'RECOGER'
    DELIVERED = 'ENTREGADA'
    
    typeDelivery = models.CharField( max_length=30 )
    products = models.ManyToManyField( Product, related_name='order', through='OrderProduct' )
    subtotal = models.DecimalField( decimal_places=2, max_digits=7 )
    tax = models.DecimalField( decimal_places=2, max_digits=7 )
    userapp = models.ForeignKey( Userapp, on_delete = models.CASCADE )
      
    def user(self):
        return self.userapp.names + ' ' + self.userapp.first_last_name + ' (' + self.userapp.alias + ')'
    
    def description(self):
        description = ''
        for oProduct in self.products.all():
            description += oProduct.name + ', '
            
        return description
    
class OrderProduct(models.Model):
    order = models.ForeignKey( Order, on_delete=models.CASCADE )
    product = models.ForeignKey( Product, on_delete=models.CASCADE )