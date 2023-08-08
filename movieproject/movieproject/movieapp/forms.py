from django import forms
from .models import movies
class FormMovie(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['name','year','desc','img']