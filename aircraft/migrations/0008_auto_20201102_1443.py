# Generated by Django 3.1.2 on 2020-11-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0007_auto_20201102_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftspec',
            name='range',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True, verbose_name='range'),
        ),
    ]
