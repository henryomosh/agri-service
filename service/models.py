from django.db import models
from django.contrib.auth.models import AbstractUser

SERVICE_PROVIDERS = (('AGROVET','Agrovet'), ('INDUSTRY', 'Industry'),('Marketing', 'Marketing'))
PRODUCT_CATEGORIES = ((1, 'Livestock' ), (2, 'Fishery'), (3, 'AgroChemicals'), (4, 'Cash Crops'), (5, 'Animal Feed'), (6, 'Tools and Equipment'),
                      (7, 'Vegetable'), (8, 'Poultry'), (9, 'Other'))


class User(AbstractUser):
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


class ServiceProvider(models.Model):
    sector = models.CharField(max_length=200, choices=SERVICE_PROVIDERS, default='AGROVET')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)


class Sell(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=PRODUCT_CATEGORIES, default=1)
    price = models.IntegerField()
    location = models.CharField(max_length=250)
    description = models.TextField()



