from django import forms
from app1.models import Stundents
class StudentsForm(forms.ModelForm):
    class Meta:
        model=Stundents
        fields="__all__"