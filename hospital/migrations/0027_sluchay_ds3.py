# Generated by Django 3.2.6 on 2022-01-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0026_auto_20220126_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='sluchay',
            name='ds3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
