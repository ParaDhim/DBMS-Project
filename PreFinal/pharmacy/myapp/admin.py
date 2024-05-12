from django.contrib import admin
from .models import *
# from CURECABIN.pharmacy.models import *
 # Register your models here.

admin.site.register(Appointment)
admin.site.register(Branches)
admin.site.register(Doctors)
admin.site.register(MedSupp)
admin.site.register(Medicalhistory)
admin.site.register(Medicines)
admin.site.register(Orders)
admin.site.register(Patients)
admin.site.register(Payment)
admin.site.register(Pharmacists)
admin.site.register(Policyprovider)
admin.site.register(PresMedicine)
admin.site.register(Prescription)
admin.site.register(Stock)
admin.site.register(Suppliers)

