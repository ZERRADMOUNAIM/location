# Generated by Django 4.2.2 on 2023-07-20 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_sys', '0006_voiture_image_alter_client_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voiture',
            name='image',
        ),
    ]