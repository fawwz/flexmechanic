# Generated by Django 4.1.7 on 2023-05-17 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_mechanic_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
