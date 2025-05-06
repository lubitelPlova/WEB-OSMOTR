from django.contrib import admin
from shop.models import Clinic, ClinicAdmin, Terminal, DeviceMeasurements, Doctor, Image, Job, Location, MedicalExamination, Patient
# Register your models here.
admin.site.register(Clinic)
admin.site.register(ClinicAdmin)
admin.site.register(DeviceMeasurements)
admin.site.register(Doctor)
admin.site.register(Image)
admin.site.register(Job)
admin.site.register(Location)
admin.site.register(MedicalExamination)
admin.site.register(Patient)
admin.site.register(Terminal)
