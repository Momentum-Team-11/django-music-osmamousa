from attr import fields
from django import forms
from .models import album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = album
        fields = [
            'title',
            'artist',
            'date_time',
        ]