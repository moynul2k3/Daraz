# Generated by Django 5.0.2 on 2024-02-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0016_alter_conversationmessage_conversation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationmessage',
            name='created_by',
        ),
    ]
