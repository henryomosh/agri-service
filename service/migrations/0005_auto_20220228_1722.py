# Generated by Django 3.2.9 on 2022-02-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_rename_photo_productimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='first_paragraph',
        ),
        migrations.AddField(
            model_name='article',
            name='fourth_paragraph',
            field=models.TextField(default='Enter text here'),
        ),
        migrations.AddField(
            model_name='article',
            name='second_paragraph',
            field=models.TextField(default='Enter text here'),
        ),
        migrations.AddField(
            model_name='article',
            name='third_paragraph',
            field=models.TextField(default='Enter text here'),
        ),
    ]
