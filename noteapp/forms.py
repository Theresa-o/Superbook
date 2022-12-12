from django import forms
from django.forms import ModelForm
from . models import Note
from ckeditor.widgets import CKEditorWidget


class NoteForm(ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control title", "placeholder": "Enter Title", "rows": "2"
    }))
    body = forms.CharField(max_length=10000, widget=CKEditorWidget(attrs={
        "class": "form-control content", "placeholder": "Enter Content", "rows": "8"
    }))

    class Meta:
        model = Note
        fields = ["title", "body", "image"]
