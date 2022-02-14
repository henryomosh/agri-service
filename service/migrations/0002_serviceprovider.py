# Generated by Django 3.2.9 on 2022-02-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(choices=[('AGROVET', 'Agrovet'), ('INDUSTRY', 'Industry')], default='AGROVET', max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=200)),
            ],
        ),
    ]
