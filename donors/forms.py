from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'name',
            'age',
            'blood_group',
            'phone',
            'location',
            'is_available'
        ]