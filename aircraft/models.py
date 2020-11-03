from django.db import models
from six import text_type
from ckeditor.fields import RichTextField

# Create your models here.
# class Manufacture(modes.Model):
#     title = models.CharField(max_length=255)
#     origin = modes.CharField(max_length=255)

class Aircraft(models.Model):
    """docstring for Aircraft."""

    manufacture_choice = (
       ('Airbus', 'Airbus'),
       ('Boeing', 'Boeing'),
       ('Lockheed Martin', 'Lockheed Martin'),
    )

    role_choice = (
       ('NBRP', 'Narrow-body Regional jet airplane'),
       ('XWB', 'Extrawide-body jet airplane'),
    )

    status_choice = (
       ('LTD', 'Limited to freighters and executive use[a]'),
       ('INS', 'In service')
    )

    poststatus_choices = (

        ('draft', 'Draft'),
        ('published', 'Published'),

    )


    # Fields
    title = models.CharField(max_length=55)
    family = models.CharField(max_length=30)
    manufacture = models.CharField(choices=manufacture_choice, max_length=55)
    role = models.CharField(choices=role_choice, max_length=100)
    slug = models.SlugField(blank=True)
    description = RichTextField()
    status = models.CharField(choices=status_choice, max_length=30)
    #media fields
    featured_photo = models.ImageField(upload_to='photos/airplanes/featured/%Y/%m/%d/', blank=True)
    photo1 = models.ImageField(upload_to='photos/airplanes/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/airplanes/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/airplanes/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/airplanes/%Y/%m/%d/', blank=True)
    #Not editable fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_featured = models.BooleanField(default=False)
    #posting record options
    poststatus = models.CharField(max_length=10, choices=poststatus_choices, default='draft')



    class Meta:
        pass

    # def __str__(self):
    #     return str(self.pk)
    def __str__(self):
        return self.manufacture + " " + self.title + "-" + self.family

    def get_absolute_url(self):
        return reverse("aircraft_Aircraft_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("aircraft_Aircraft_update", args=(self.slug,))


class AircraftSpec(models.Model):


     engines_choices = (
         ('RRTrentXWB337kN (74,000 LBF)', 'RR Trent XWB 337kN (74,000 LBF)'),
         ('RRTrentXWB374kN (83,000 LBF)', 'RR Trent XWB 374kN (83,000 LBF)'),
         ('RRTrentXWB432kN (97,000 LBF)', 'RR Trent XWB 432kN (97,000 LBF)'),
     )

     msrmnt_attrs = {'max_digits': 6,
                'decimal_places': 3,
                'blank': True,
                'null': True}


     type = models.OneToOneField(Aircraft, on_delete = models.CASCADE, primary_key = True)
     range = models.DecimalField(('Range'), **msrmnt_attrs)
     seating = models.IntegerField(('Seating'), null=True, blank=True)
     replaces_current_model = models.CharField(max_length=30, blank=True)
     competes_against = models.CharField(max_length=30, blank=True)
     length = models.DecimalField(('Length'), **msrmnt_attrs)
     wing_span = models.DecimalField(('Wing_span'), **msrmnt_attrs)
     height = models.DecimalField(('Height'), **msrmnt_attrs)
     fuselage_width_ext = models.DecimalField(('Fuselage width exterior'), **msrmnt_attrs)
     cabin_width_Int = models.DecimalField(('Cabin width interior'), **msrmnt_attrs)
     track = models.DecimalField(('Track'), **msrmnt_attrs)
     wheelbase = models.DecimalField(('wheelbase'), **msrmnt_attrs)
     maximum_operating_speed = models.DecimalField(('Maximum operating speed'), **msrmnt_attrs)
     maximum_ramp_weight = models.DecimalField(('Maximum ramp weight'), **msrmnt_attrs)
     maximum_take_off_weight = models.DecimalField(('Maximum take off weight'), **msrmnt_attrs)
     maximum_landing_weight = models.DecimalField(('Maximum landing weight'), **msrmnt_attrs)
     maximum_zero_fuel_weight = models.DecimalField(('Maximum zero fuel weight'), **msrmnt_attrs)
     maximum_fuel_capacity = models.DecimalField(('Maximum fuel capacity'), **msrmnt_attrs)
     engines = models.CharField(choices=engines_choices, blank=True, max_length=55, )
     average_unit_price = models.CharField(max_length=15, blank=True)
     def __str__(self, ):
        return str(self.type)

     # def __unicode__(self):
     #    return self.type

     class Meta:
        verbose_name = "Aircraft Specification"




# class AircraftFreightCapacity(models.Model):
#     type = models.OneToOneField(Aircraft, on_delete = models.CASCADE, primary_key = True)
#     cargo_compartment_cpct_ld3 =
