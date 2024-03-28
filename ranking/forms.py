from django import forms
from multiupload.fields import MultiFileInput
from .models import Image


class MultipleImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['images']

    images = forms.FileField(widget=MultiFileInput(attrs={'multiple': True}))
