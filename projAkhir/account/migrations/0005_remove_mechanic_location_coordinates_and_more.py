# Generated by Django 4.1.7 on 2023-05-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_mechanic_owner_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mechanic',
            name='location_coordinates',
        ),
        migrations.RemoveField(
            model_name='mechanic',
            name='location_name',
        ),
        migrations.RemoveField(
            model_name='mechanic',
            name='photo',
        ),
        migrations.AddField(
            model_name='mechanic',
            name='owner_nik',
            field=models.CharField(default='300xxxxxxxxxxxx', max_length=15),
        ),
    ]