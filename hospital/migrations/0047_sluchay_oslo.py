# Generated by Django 3.2.6 on 2022-05-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0046_remove_sluchay_oslo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sluchay',
            name='oslo',
            field=models.ManyToManyField(blank=True, to='hospital.Oslo'),
        ),
    ]
