# Generated by Django 3.2.23 on 2024-01-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20240104_0832'),
        ('wishitem', '0002_auto_20240103_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishitem',
            name='products',
            field=models.ManyToManyField(through='wishitem.WishitemProduct', to='products.Product'),
        ),
    ]
