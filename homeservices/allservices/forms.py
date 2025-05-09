from django import forms
from .models import ServiceBooking

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = ServiceBooking
        fields = ['name', 'email', 'phone', 'address', 'preferred_date', 'note']  # Removed 'service'
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        self.service_type = kwargs.pop('service_type', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.service = self.service_type  # Set service from URL parameter
        if commit:
            instance.save()
        return instance