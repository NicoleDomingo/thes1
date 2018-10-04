# Generated by Django 2.0.5 on 2018-09-26 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0010_auto_20180926_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartrate',
            name='idPatient',
        ),
        migrations.RemoveField(
            model_name='heartrate',
            name='idRefHeart',
        ),
        migrations.RemoveField(
            model_name='patient_table',
            name='idBeds',
        ),
        migrations.RemoveField(
            model_name='patient_table',
            name='idPatient',
        ),
        migrations.RemoveField(
            model_name='position',
            name='idPatient',
        ),
        migrations.DeleteModel(
            name='Ref_BedStatus',
        ),
        migrations.DeleteModel(
            name='Ref_PatientStatus',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='idPatient',
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
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Patient_Table',
        ),
        migrations.DeleteModel(
            name='Position',
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
