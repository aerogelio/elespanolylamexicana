from django.db import models

class Tax( models.Model ):    
    name = models.CharField( max_length=30 )
    description = models.CharField( max_length=70 )
    percentage = models.DecimalField( decimal_places=2, max_digits=5 )
    
    def __str__(self):
        return self.name + ', ' + self.description