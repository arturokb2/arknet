# Generated by Django 3.2.6 on 2022-01-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0027_sluchay_ds3'),
    ]

    operations = [
        migrations.AddField(
            model_name='sluchay',
            name='code_mes1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sluchay',
            name='code_mes2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
