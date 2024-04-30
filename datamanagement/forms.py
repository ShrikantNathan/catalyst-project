from .models import UserQuery, UserModel
from django.forms import Form, FileField, ModelForm
from django import forms


class UploadForm(Form):
    file = FileField()

class QueryForm(ModelForm):
    class Meta:
        model = UserQuery
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class UserModelForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email_address", "status"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email_address": forms.TextInput(attrs={'class': 'form-control'}),
            "status": forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }