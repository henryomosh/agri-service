# Generated by Django 3.2.9 on 2022-02-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20220228_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='fourth_paragraph',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='second_paragraph',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='third_paragraph',
            field=models.TextField(default=''),
        ),
    ]
