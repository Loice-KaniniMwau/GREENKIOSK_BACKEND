# Generated by Django 4.2.3 on 2023-08-06 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customer_image'),
        ('payment', '0002_payment_amount_payment_nameofpayee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='nameofPayee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]