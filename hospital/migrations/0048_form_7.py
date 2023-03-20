# Generated by Django 3.2.6 on 2022-06-07 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okb2', '0018_v036'),
        ('hospital', '0047_sluchay_oslo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.otde')),
                ('prof_k', models.ManyToManyField(blank=True, to='okb2.V020')),
            ],
        ),
    ]
