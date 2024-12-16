from django.contrib import admin
from .models import Doctor, Symptom, Appointment, Contact

admin.site.register(Doctor)
admin.site.register(Symptom)
admin.site.register(Appointment)
admin.site.register(Contact)