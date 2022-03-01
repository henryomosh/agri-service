from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

SERVICE_PROVIDERS = (('Agrovet','Agrovet'), ('Industry', 'Industry'),('Marketer', 'Marketer'))
PRODUCT_CATEGORIES = (('livestock', 'Livestock'), ('fishery', 'Fishery'), ('agroChemicals', 'AgroChemicals'),
                      ('crops', 'Cash Crops'),('feeds', 'Animal Feed'), ('tools', 'Tools and Equipment'),
                      ('vegetables', 'Vegetables'), ('poultry', 'Poultry'), ('other', 'Other'))

USER_TYPE = (('Farmer', 'Farmer'), ('Agrovet', 'Agrovet'), ('Industry', 'Industry Agent'), ('Marketer', 'Marketer'))

LOCATION = (('Njoro', 'Njoro'),('Naivasha', 'Naivasha'), ('Nakuru-Town-East', 'Nakuru Town East'),
            ('Nakuru-Town-West', 'Nakuru Town West'), ('Bahati', 'Bahati'), ('Gilgil', 'Gilgil')
            , ('Kuresoi-North', 'Kuresoi North'), ('Lanet', 'Lanet'), ('London', 'London'))


class User(AbstractUser):
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    you_are_a = models.CharField(max_length=200, choices=USER_TYPE)


class Sell(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sell_products')
    product_name = models.CharField(max_length=200)
    category = models.TextField(choices=PRODUCT_CATEGORIES)
    price = models.IntegerField()
    location = models.CharField(max_length=200, choices=LOCATION)
    description = models.TextField()
    image = models.FileField(upload_to='products/', null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])


class ProductImage(models.Model):
    name = models.ForeignKey(Sell, on_delete=models.CASCADE, null=True, blank=True, related_name='product_image')
    image = models.FileField(upload_to='products/images/', null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_name')
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    first_paragraph = models.TextField()
    second_paragraph = models.TextField(default='')
    third_paragraph = models.TextField(default='')
    fourth_paragraph = models.TextField(default='')
    block_quote = models.TextField()
    date = models.DateField()
    image = models.FileField(upload_to='articles/', null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])


class ArticleImage(models.Model):
    name = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='articles/images/', null=True, blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])






