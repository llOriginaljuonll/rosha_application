# Generated by Django 5.0.6 on 2024-10-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0003_alter_audition_announcement_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='announcement_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audition',
            name='concert_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audition',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]