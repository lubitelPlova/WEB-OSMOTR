from django.contrib import admin
from shop.models import Clinic, Clinicadmin, Terminal, Devicemeasurements, Doctor, Image, Job, Location, Medicalexamination, Patient
# Register your models here.
admin.site.register(Clinic)
admin.site.register(Clinicadmin)
admin.site.register(Devicemeasurements)
admin.site.register(Doctor)
admin.site.register(Image)
admin.site.register(Job)
admin.site.register(Location)
admin.site.register(Medicalexamination)
admin.site.register(Patient)
