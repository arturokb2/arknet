# Generated by Django 3.2.6 on 2022-10-17 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okb2', '0019_otde_number_beds'),
        ('hospital', '0058_alter_oper_oslo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sluchay',
            name='ksg_osn2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ksg_osn2', to='okb2.group_kc_group'),
        ),
    ]
