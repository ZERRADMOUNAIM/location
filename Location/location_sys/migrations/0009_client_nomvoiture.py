# Generated by Django 4.2.2 on 2023-07-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_sys', '0008_voiture_prix'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='NomVoiture',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]