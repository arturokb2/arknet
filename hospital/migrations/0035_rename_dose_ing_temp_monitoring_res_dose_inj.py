# Generated by Django 3.2.6 on 2022-01-31 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0034_temp_monitoring_res_date_inj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temp_monitoring_res',
            old_name='dose_ing',
            new_name='dose_inj',
        ),
    ]
