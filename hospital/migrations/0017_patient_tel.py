# Generated by Django 3.2.6 on 2022-01-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_auto_20220126_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='tel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
