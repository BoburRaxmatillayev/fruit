# Generated by Django 5.0.6 on 2024-05-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=4),
        ),
    ]
