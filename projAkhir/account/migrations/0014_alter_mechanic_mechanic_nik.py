# Generated by Django 4.2.1 on 2023-05-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_mechanic_mechanic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='mechanic_nik',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
