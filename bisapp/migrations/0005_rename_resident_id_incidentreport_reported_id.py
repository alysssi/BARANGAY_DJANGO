# Generated by Django 4.2.7 on 2023-12-09 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bisapp', '0004_alter_incidentreport_report_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidentreport',
            old_name='resident_id',
            new_name='reported_id',
        ),
    ]
