# Generated by Django 5.0.6 on 2024-10-03 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditioner', '0005_delete_performresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditioner',
            name='personal_info',
        ),
        migrations.RemoveField(
            model_name='auditioner',
            name='regis_confirm',
        ),
    ]