# Generated by Django 4.2.3 on 2023-08-09 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_image'),
        ('payment', '0009_remove_payment_nameofpayee_payment_nameofpayee'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
    ]