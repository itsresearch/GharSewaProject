# allservices/forms.py
from django import forms
from .models import ServiceBooking

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['name', 'email', 'phone', 'address', 'service_type', 'preferred_date']
