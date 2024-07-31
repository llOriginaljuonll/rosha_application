# Generated by Django 5.0.6 on 2024-07-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrant', '0002_entrant_pers_info_entrant_slip_alter_entrant_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrant',
            old_name='entity_name',
            new_name='prim_contact',
        ),
        migrations.AlterField(
            model_name='entrant',
            name='entity',
            field=models.CharField(choices=[('', 'Choose one of the following options'), ('1', 'Individual (apply is alone)'), ('2', 'Group (apply as a team)')], max_length=100),
        ),
    ]
