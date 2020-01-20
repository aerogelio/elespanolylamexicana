import decimal
from django.db import models
from elespanolylamexicanaapp.models.tax import Tax
from elespanolylamexicanaapp.models.category import Category

class Product(models.Model):
    
    name = models.CharField( max_length=30)
    description = models.CharField(max_length=70)
    image = models.ImageField( upload_to='' )
    price = models.DecimalField( max_digits= 5, decimal_places=2 )
    
    taxes = models.ManyToManyField( Tax, related_name="products" )
    category = models.ForeignKey( Category, on_delete=models.CASCADE )
    
    def total(self):
        total = decimal.Decimal(0.00)
        for tax in self.taxes.all():
            total += (self.price * (tax.percentage/decimal.Decimal('100')))
        total += self.price
        return round(total, 2)
    
    def iva_Html(self):
        strIvaHtml = ""
        
        for i, tax in enumerate(self.taxes.all()):
            strIvaHtml += tax.name + ', '
        
        return strIvaHtml
    
    def __str__(self):
        return self.name + ', ' + self.description