# Generated by Django 3.2.6 on 2022-01-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okb2', '0003_auto_20220124_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='code_med_dev',
            name='datebeg',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='code_med_dev',
            name='dateend',
            field=models.DateField(blank=True, null=True),
        ),
    ]
