from rest_framework import serializers
from .models import Dentist, Patient, Appointment, Treatment, AppointmentHistory, Payment

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class AppointmentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentHistory
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

