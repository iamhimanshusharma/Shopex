from django.db import models

# Create your models here.
class People(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Shop(models.Model):
    email = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)
    shop_id = models.CharField(max_length=50)
    shop_pic = models.ImageField(upload_to='shop/', default='profile.png')