# Generated by Django 2.0.5 on 2018-09-25 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageBed', '0008_auto_20180925_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageBed.Ref_PatientStatus'),
        ),
    ]
