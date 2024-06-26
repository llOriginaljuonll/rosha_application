# Generated by Django 5.0.6 on 2024-06-04 19:32

import django.core.validators
import django.db.models.deletion
import embed_video.fields
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^[0-9]')])),
                ('email', models.EmailField(max_length=254)),
                ('school', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/', verbose_name='Image')),
                ('instrument', models.CharField(max_length=255)),
                ('song', models.CharField(max_length=255)),
                ('shorts_url', embed_video.fields.EmbedVideoField(blank=True)),
                ('cpr_permission', models.BooleanField()),
                ('regis_confirm', models.BooleanField()),
                ('slip', versatileimagefield.fields.VersatileImageField(upload_to='slip/', verbose_name='Slip')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.competition')),
            ],
        ),
    ]
