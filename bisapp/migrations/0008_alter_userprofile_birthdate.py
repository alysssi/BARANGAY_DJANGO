# Generated by Django 4.2.7 on 2023-12-11 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bisapp', '0007_contact_alter_incidentreport_reporter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
