# Generated by Django 3.1.2 on 2020-11-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0012_auto_20201102_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftspec',
            name='range',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='range'),
        ),
    ]
