# Generated by Django 3.1.2 on 2020-11-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0016_auto_20201102_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircraftspec',
            options={'verbose_name': 'Aircraft Specification'},
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='average_unit_price',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='cabin_width_Int',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Cabin width interior'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='competes_against',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='engines',
            field=models.CharField(blank=True, choices=[('RRTrentXWB337kN (74,000 LBF)', 'RR Trent XWB 337kN (74,000 LBF)'), ('RRTrentXWB374kN (83,000 LBF)', 'RR Trent XWB 374kN (83,000 LBF)'), ('RRTrentXWB432kN (97,000 LBF)', 'RR Trent XWB 432kN (97,000 LBF)')], max_length=55),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='fuselage_width_ext',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Fuselage width exterior'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Length'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='maximum_fuel_capacity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Maximum fuel capacity'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='maximum_landing_weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Maximum landing weight'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='maximum_operating_speed',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Maximum operating speed'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='maximum_ramp_weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Maximum ramp weight'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='maximum_take_off_weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Maximum take off weight'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='maximum_zero_fuel_weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Maximum zero fuel weight'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='replaces_current_model',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='seating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Seating'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='track',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Track'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='wheelbase',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='wheelbase'),
        ),
        migrations.AddField(
            model_name='aircraftspec',
            name='wing_span',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Wing_span'),
        ),
        migrations.AlterField(
            model_name='aircraftspec',
            name='range',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Range'),
        ),
    ]