from django import forms
from .models import Contact  # Make sure Contact model exists in models.py

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']