# Generated by Django 2.0.5 on 2018-09-25 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0005_auto_20180925_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartrate',
            name='idRefHeart',
        ),
        migrations.RemoveField(
            model_name='patient_table',
            name='idBeds',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='Ref_BedStatus',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='idRef',
        ),
        migrations.DeleteModel(
            name='Beds',
        ),
        migrations.DeleteModel(
            name='HeartRate',
        ),
        migrations.DeleteModel(
            name='Patient_Table',
        ),
        migrations.DeleteModel(
            name='Ref_HeartRate',
        ),
        migrations.DeleteModel(
            name='Ref_Temp',
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
    ]
