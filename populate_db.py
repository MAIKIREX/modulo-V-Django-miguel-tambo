import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dentalclinic.settings')
django.setup()

from django.contrib.auth.models import User
from appointments.models import Dentist, Patient, Appointment, Treatment, AppointmentHistory, Payment

# Crear usuarios
user1 = User.objects.create_user(username='dentist1', password='password123', first_name='John', last_name='Doe', email='john@example.com')
user2 = User.objects.create_user(username='patient1', password='password123', first_name='Jane', last_name='Smith', email='jane@example.com')

# Crear dentista
dentist1 = Dentist.objects.create(user=user1, specialization='Orthodontist')

# Crear paciente
patient1 = Patient.objects.create(user=user2, phone='1234567890', address='123 Main St')

# Crear cita
appointment1 = Appointment.objects.create(dentist=dentist1, patient=patient1, date=datetime.date(2024, 8, 1), time=datetime.time(10, 0), reason='Regular Checkup', confirmed=True)

# Crear tratamiento
treatment1 = Treatment.objects.create(appointment=appointment1, description='Teeth Cleaning', cost=100.00)

# Crear historial de citas
history1 = AppointmentHistory.objects.create(appointment=appointment1, status='Completed', comments='Patient is in good health.')

# Crear pago
payment1 = Payment.objects.create(treatment=treatment1, amount=100.00, method='Credit Card')

print("Datos de ejemplo añadidos exitosamente.")
