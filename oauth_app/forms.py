from django import forms
from .models import MyFile


class MyFileForm(forms.ModelForm):
    class Meta:
        model = MyFile
        fields = ('title', 'description', 'file','name')


class MyFileUpdateForm(forms.ModelForm):
    class Meta:
        model = MyFile
        fields = ['status', 'admin_notes']
