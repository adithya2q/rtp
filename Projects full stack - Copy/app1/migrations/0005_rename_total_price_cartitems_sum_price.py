# Generated by Django 3.2.23 on 2023-12-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_cartitems_seller_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='total_price',
            new_name='Sum_price',
        ),
    ]
