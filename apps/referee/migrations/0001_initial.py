# Generated by Django 5.0.6 on 2024-07-03 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auditioner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_score', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('rythm_score', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('perform_score', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('average', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('auditioner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auditioner.auditioner')),
            ],
        ),
    ]
