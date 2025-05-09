from django import forms
from .models import ServiceBooking

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['name', 'email', 'phone', 'address', 'service', 'preferred_date', 'note']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4}),
        }