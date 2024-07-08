# Generated by Django 5.0.6 on 2024-07-05 07:01

import django.db.models.deletion
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participation', '0002_participation_category_participation_create_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=255)),
                ('length_of_song', models.TimeField()),
                ('accompanist', models.CharField(max_length=255)),
                ('award_history', models.CharField(max_length=1000)),
                ('english_skill', models.CharField(max_length=255)),
                ('people_coming', models.IntegerField()),
                ('plan_comming', models.CharField(max_length=1000)),
                ('practice_room', models.BooleanField()),
                ('cpr_permission', models.BooleanField()),
                ('regis_confirm', models.BooleanField()),
                ('slip', versatileimagefield.fields.VersatileImageField(upload_to='slip/', verbose_name='Slip')),
                ('participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participation.participation')),
            ],
        ),
    ]