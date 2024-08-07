# Generated by Django 5.0.6 on 2024-07-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='comp_poster',
            new_name='compt_poster',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='compet_date',
        ),
        migrations.AddField(
            model_name='competition',
            name='ann_time',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='compt_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='compt_time',
            field=models.TimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='deadline_time',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='ann_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='descr_payment',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='elig',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='instr_type',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
