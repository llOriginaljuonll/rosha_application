# Generated by Django 5.0.6 on 2024-10-03 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0004_remove_participant_auditioner_participant_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='regis_confirm',
        ),
    ]
