# Generated by Django 3.2.23 on 2023-12-26 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_rename_total_price_cartitems_sum_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField(max_length=12)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField(max_length=10)),
                ('Total_price', models.IntegerField()),
                ('Payment_mode', models.CharField(max_length=140)),
                ('Payment_id', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(choices=[('pending', 'pending'), ('Out for shipping', 'Out for shipping'), ('completed', 'completed')], default='pending', max_length=140)),
                ('Message', models.CharField(max_length=540, null=True)),
                ('Tracking_id', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
