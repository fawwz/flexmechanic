# Generated by Django 4.2.1 on 2023-05-31 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_mechanic_mechanic_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='mechanic_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='mechanic_nik',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
