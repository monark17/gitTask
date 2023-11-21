# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
