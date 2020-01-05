from django.db import models
from django.contrib.auth.models import User

class Userapp(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    names = models.CharField( max_length=150 )
    first_last_name = models.CharField( max_length=150 )
    second_last_name = models.CharField( max_length=150 )
    alias = models.CharField( max_length=150 )