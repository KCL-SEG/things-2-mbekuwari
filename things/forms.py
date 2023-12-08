"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    # Customizing widget for description and quantity fields
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        'quantity': forms.NumberInput(attrs={'min': 0, 'max': 100}),
    }