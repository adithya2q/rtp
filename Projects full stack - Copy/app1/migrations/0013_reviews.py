# Generated by Django 3.2.23 on 2023-12-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_orderdetails_tracking_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Review', models.TextField()),
            ],
        ),
    ]
