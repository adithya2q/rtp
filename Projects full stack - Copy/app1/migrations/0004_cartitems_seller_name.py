# Generated by Django 3.2.23 on 2023-12-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_cartitems_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='seller_name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
