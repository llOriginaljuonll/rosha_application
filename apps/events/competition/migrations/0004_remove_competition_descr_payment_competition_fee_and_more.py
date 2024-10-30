# Generated by Django 5.0.6 on 2024-10-30 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_alter_competition_ann_time_and_more'),
        ('hall', '0003_remove_hall_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='descr_payment',
        ),
        migrations.AddField(
            model_name='competition',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='hall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hall.hall'),
        ),
    ]
