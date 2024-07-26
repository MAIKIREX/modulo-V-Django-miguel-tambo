from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DentistViewSet, PatientViewSet, AppointmentViewSet, TreatmentViewSet, AppointmentHistoryViewSet, PaymentViewSet, Appointment_count

router = DefaultRouter()
router.register(r'dentists', DentistViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'treatments', TreatmentViewSet)
router.register(r'appointmenthistories', AppointmentHistoryViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    *router.urls,
    path('Appointment/cantidad/', Appointment_count)
]
