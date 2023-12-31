"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        'quantity': forms.NumberInput()
        }

    # Customizing widget for description and quantity fields
