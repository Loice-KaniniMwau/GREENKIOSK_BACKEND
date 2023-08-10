# Generated by Django 4.2.3 on 2023-08-09 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_image'),
        ('shoppingcart', '0005_shoppingcart_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='customer',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='productS',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
