# Generated by Django 5.0.6 on 2024-07-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participation', '0002_participation_category_participation_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
