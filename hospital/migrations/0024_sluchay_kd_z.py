# Generated by Django 3.2.6 on 2022-01-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0023_auto_20220126_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='sluchay',
            name='kd_z',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
