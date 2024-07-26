from django.contrib import admin
from .models import Dentist, Patient, Appointment, Treatment, AppointmentHistory, Payment

admin.site.register(Dentist)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Treatment)
admin.site.register(AppointmentHistory)
admin.site.register(Payment)
