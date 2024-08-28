# Generated by Django 5.1 on 2024-08-23 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('outflows', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outflow',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Produto'),
        ),
    ]
