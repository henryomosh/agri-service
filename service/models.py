from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

SERVICE_PROVIDERS = (('AGROVET','Agrovet'), ('INDUSTRY', 'Industry'),('Marketing', 'Marketing'))
PRODUCT_CATEGORIES = ((1, 'Livestock' ), (2, 'Fishery'), (3, 'AgroChemicals'), (4, 'Cash Crops'), (5, 'Animal Feed'), (6, 'Tools and Equipment'),
                      (7, 'Vegetable'), (8, 'Poultry'), (9, 'Other'))

USER_TYPE = ((1, 'farmer'), (2, 'agrovet'), (3, 'industry_agent'), (4, 'marketer'))


class User(AbstractUser):
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    you_are = models.CharField(max_length=200, choices=USER_TYPE, default=1)


# class SellImages(models.Model):
#     image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])


class Sell(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sell_products')
    product_name = models.CharField(max_length=200)
    category = models.IntegerField(choices=PRODUCT_CATEGORIES)
    price = models.IntegerField()
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_name')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    image = models.FileField()







