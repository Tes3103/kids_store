# Generated by Django 3.2.23 on 2024-01-03 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_sizes'),
        ('wishitem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishitem',
            name='quantity',
        ),
        migrations.CreateModel(
            name='WishitemProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('wishitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishitem.wishitem')),
            ],
        ),
        migrations.AddField(
            model_name='wishitem',
            name='products',
            field=models.ManyToManyField(through='wishitem.WishitemProduct', to='products.Product'),
        ),
    ]