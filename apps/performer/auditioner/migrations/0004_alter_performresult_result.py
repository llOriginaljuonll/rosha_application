# Generated by Django 5.0.6 on 2024-07-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditioner', '0003_performresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performresult',
            name='result',
            field=models.CharField(max_length=255),
        ),
    ]
