# Generated by Django 5.1.5 on 2025-02-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_customer_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
