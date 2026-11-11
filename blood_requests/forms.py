
from django import forms
from .models import BloodRequest
from donors.models import Donor


class BloodRequestForm(forms.ModelForm):

    class Meta:
        model = BloodRequest
        fields = [
            'donor',
            'patient_name',
            'blood_group',
            'units',
            'hospital',
            'location',
            'contact_number',
        ]

        widgets = {
            'donor': forms.Select(attrs={
                'class': 'form-select'
            }),
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter patient name'
            }),
            'blood_group': forms.Select(attrs={
                'class': 'form-select'
            }),
            'units': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'hospital': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hospital name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['donor'].queryset = Donor.objects.filter(
            is_available=True,
            user__isnull=False
        ).order_by('name')

        self.fields['donor'].empty_label = 'Select a donor'
