# Generated by Django 3.2.9 on 2022-02-26 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20220226_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='photo',
        ),
    ]
