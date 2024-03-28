from django import forms
from .models import Audio


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title','audio']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter Audio title',
                'style': 'background-color: white; border-radius: 25px;',
            }),
            'audio': forms.ClearableFileInput(attrs={
                'accept': 'audio/wav',  # Specify accepted file types (optional)
                'class': 'custom-file-input',  # Apply a custom CSS class
                'style': 'border: 2px solid #3498db; padding: 8px; border-radius: 8px;',  # Custom styling
            }),
        }