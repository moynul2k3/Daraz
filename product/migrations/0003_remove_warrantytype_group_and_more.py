# Generated by Django 5.0.2 on 2024-02-09 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warrantytype',
            name='group',
        ),
        migrations.RemoveField(
            model_name='warrantytype',
            name='subcategory',
        ),
    ]