# Generated by Django 4.2.2 on 2023-07-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_sys', '0004_alter_client_cne'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='reserver',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
