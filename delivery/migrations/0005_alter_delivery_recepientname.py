# Generated by Django 4.2.3 on 2023-08-14 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0004_alter_delivery_recepientname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='recepientname',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
