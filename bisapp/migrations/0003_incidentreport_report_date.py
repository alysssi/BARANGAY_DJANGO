# Generated by Django 4.2.7 on 2023-12-09 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bisapp', '0002_incidentreport_resident_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='report_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]