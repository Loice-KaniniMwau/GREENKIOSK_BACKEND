# Generated by Django 4.2.3 on 2023-08-06 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customer_image'),
        ('payment', '0003_alter_payment_nameofpayee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='nameofPayee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]