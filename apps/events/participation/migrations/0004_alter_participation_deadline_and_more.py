# Generated by Django 5.0.6 on 2024-10-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participation', '0003_participation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participation',
            name='rehearsal_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]