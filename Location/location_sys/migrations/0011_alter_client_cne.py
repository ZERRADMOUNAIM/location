# Generated by Django 4.2.3 on 2023-07-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_sys', '0010_voiture_carimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='CNE',
            field=models.CharField(default='', max_length=70),
        ),
    ]
