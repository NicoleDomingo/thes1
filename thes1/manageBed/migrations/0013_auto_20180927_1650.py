# Generated by Django 2.0.5 on 2018-09-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0012_auto_20180926_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
