# Generated by Django 3.2.23 on 2023-12-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_orderdetails_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='Phone',
            field=models.CharField(max_length=12),
        ),
    ]