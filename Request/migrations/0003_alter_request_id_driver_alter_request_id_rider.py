# Generated by Django 4.1.7 on 2023-04-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0002_alter_request_time_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='id_driver',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='id_rider',
            field=models.IntegerField(null=True),
        ),
    ]
