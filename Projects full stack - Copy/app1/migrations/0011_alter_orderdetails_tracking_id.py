# Generated by Django 3.2.23 on 2023-12-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_price_at_purchase_orderitems_unit_price_at_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='Tracking_id',
            field=models.CharField(max_length=150),
        ),
    ]