# Generated by Django 3.2.6 on 2022-01-25 09:27

from django.db import migrations, models
import hospital.validators


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_delete_load'),
    ]

    operations = [
        migrations.AddField(
            model_name='load_1c',
            name='sluch_10',
            field=models.FileField(blank=True, null=True, upload_to='documents/hospital/%Y/%m/%d', validators=[hospital.validators.validate_file]),
        ),
        migrations.AlterField(
            model_name='load_1c',
            name='oper',
            field=models.FileField(blank=True, null=True, upload_to='documents/hospital/%Y/%m/%d', validators=[hospital.validators.validate_file]),
        ),
        migrations.AlterField(
            model_name='load_1c',
            name='sluch',
            field=models.FileField(blank=True, null=True, upload_to='documents/hospital/%Y/%m/%d', validators=[hospital.validators.validate_file]),
        ),
    ]
