# Generated by Django 4.1.7 on 2023-04-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0004_request_distance_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='id_driver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='id_rider',
            field=models.IntegerField(default=0),
        ),
    ]