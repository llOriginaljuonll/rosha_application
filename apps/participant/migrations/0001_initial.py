# Generated by Django 5.0.6 on 2024-07-03 04:07

import django.core.validators
import django.db.models.deletion
import embed_video.fields
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.TextField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('age', models.IntegerField(blank=True, null=True)),
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
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
