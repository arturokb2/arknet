# Generated by Django 3.2.6 on 2022-04-01 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okb2', '0016_v014_kod'),
        ('hospital', '0041_alter_sluchay_vds'),
    ]

    operations = [
        migrations.AddField(
            model_name='sluchay',
            name='dskz2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dskz2', to='okb2.ds'),
        ),
    ]
