# Generated by Django 5.0.2 on 2024-02-21 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0014_alter_conversationmessage_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='conversation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='messaging.conversation'),
            preserve_default=False,
        ),
    ]
