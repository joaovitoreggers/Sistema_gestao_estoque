# Generated by Django 5.1 on 2024-08-23 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_suppliers_delete_brand'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suppliers',
            new_name='Brand',
        ),
    ]
