# Generated by Django 4.0.6 on 2022-07-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_vehicle_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='bodyClass',
            field=models.CharField(max_length=100),
        ),
    ]
