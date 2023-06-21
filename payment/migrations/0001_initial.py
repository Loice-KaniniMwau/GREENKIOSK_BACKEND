# Generated by Django 4.2.1 on 2023-06-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentmethod', models.CharField(choices=[('mpesa', 'Mpesa'), ('cash', 'Cash')], max_length=32)),
                ('paymentstatus', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('cancelled', 'Canclled')], max_length=32)),
                ('datepaid', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
