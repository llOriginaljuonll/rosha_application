# Generated by Django 5.0.6 on 2024-07-23 17:43

import django.core.validators
import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0003_alter_competition_ann_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nat', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^[0-9]')])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=255)),
                ('school', models.CharField(max_length=100)),
                ('entity', models.CharField(max_length=100)),
                ('entity_name', models.CharField(max_length=255)),
                ('elig', models.CharField(max_length=255)),
                ('instr_type', models.CharField(max_length=255)),
                ('songs', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv', 'flv'])])),
                ('short_url', embed_video.fields.EmbedVideoField(blank=True)),
                ('cpr', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('compt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.competition')),
            ],
        ),
    ]
