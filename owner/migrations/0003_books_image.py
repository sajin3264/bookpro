# Generated by Django 4.0.2 on 2022-03-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_rename_price_books_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]