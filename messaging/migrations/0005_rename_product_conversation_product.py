# Generated by Django 5.0.2 on 2024-02-20 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_remove_conversation_receiver_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='Product',
            new_name='product',
        ),
    ]