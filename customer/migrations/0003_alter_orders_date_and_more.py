# Generated by Django 4.0.2 on 2022-04-04 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.timedelta(days=5), null=True),
        ),
    ]
