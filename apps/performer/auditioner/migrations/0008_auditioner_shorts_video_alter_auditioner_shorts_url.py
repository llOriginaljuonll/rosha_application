# Generated by Django 5.0.6 on 2024-10-30 20:50

import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditioner', '0007_auditioner_applicant_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditioner',
            name='shorts_video',
            field=models.FileField(blank=True, null=True, upload_to='auditioner/{id}'),
        ),
        migrations.AlterField(
            model_name='auditioner',
            name='shorts_url',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]