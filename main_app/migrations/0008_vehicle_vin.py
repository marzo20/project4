# Generated by Django 4.0.6 on 2022-07-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_trim_vehicle_bodyclass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(default=None, max_length=17),
        ),
    ]
