# Generated by Django 4.2.1 on 2023-06-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
                ('category_type', models.CharField(max_length=32)),
                ('quantity_stocked', models.PositiveIntegerField()),
            ],
        ),
    ]
