# Generated by Django 4.1.7 on 2023-04-26 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_mechanic_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='owner_name',
            field=models.CharField(default='INSERT FULL NAME', max_length=100),
        ),
    ]