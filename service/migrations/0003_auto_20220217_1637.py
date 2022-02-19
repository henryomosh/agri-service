# Generated by Django 3.2.9 on 2022-02-17 13:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_serviceprovider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('category', models.IntegerField(choices=[(1, 'Livestock'), (2, 'Fishery'), (3, 'AgroChemicals'), (4, 'Cash Crops'), (5, 'Animal Feed'), (6, 'Tools and Equipment'), (7, 'Vegetable'), (8, 'Poultry'), (9, 'Other')])),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ServiceProvider',
        ),
    ]