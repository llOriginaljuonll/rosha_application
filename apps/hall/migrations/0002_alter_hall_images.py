# Generated by Django 5.0.6 on 2024-10-22 07:24

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='images',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default=list, upload_to=''),
        ),
    ]