# Generated by Django 3.2.6 on 2022-02-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0039_le_vr_aro_let'),
    ]

    operations = [
        migrations.AlterField(
            model_name='le_vr',
            name='aro_let',
            field=models.CharField(blank=True, choices=[('1', '1 - в течение 1 часа'), ('2', '2 - в течение 1 суток'), ('3', '3 - более чем через 1 сутки')], max_length=1, null=True),
        ),
    ]
