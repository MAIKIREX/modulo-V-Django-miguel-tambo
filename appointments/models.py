from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Validadores personalizados
def validate_phone(value):
    if not value.isdigit():
        raise ValidationError('El número de teléfono debe contener solo dígitos.')

def validate_positive(value):
    if value <= 0:
        raise ValidationError('El valor debe ser positivo.')

# Modelos de la base de datos

class Dentist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.specialization}'

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, validators=[validate_phone])
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.get_full_name()}'

class Appointment(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=255)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'Appointment for {self.patient.user.get_full_name()} with {self.dentist.user.get_full_name()} on {self.date} at {self.time}'

class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_positive])

    def __str__(self):
        return f'Treatment for {self.appointment}'

class AppointmentHistory(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # Ej. 'Completed', 'Cancelled'
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'History for {self.appointment}'

class Payment(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_positive])
    payment_date = models.DateField(auto_now_add=True)
    method = models.CharField(max_length=50)  # Ej. 'Credit Card', 'Cash'

    def __str__(self):
        return f'Payment of {self.amount} for {self.treatment}'
