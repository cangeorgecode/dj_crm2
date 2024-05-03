from django import forms
from .models import *
from django.forms import FileField, Form

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name", "class": "form-control", "label": " "}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Last name", "class": "form-control", "label": " "}))
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control", "label": " "}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control", "label": " "}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control", "label": " "}))

    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'address', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].help_text = ''

        self.fields['address'].label = ''
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].help_text = ''

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].help_text = ''

        self.fields['phone'].label = ''
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].help_text = ''

class UploadForm(Form):
    records_file = FileField()

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)

        self.fields['records_file'].label = 'Accepts csv file only'
        self.fields['records_file'].widget.attrs['class'] = 'form-control'
        self.fields['records_file'].widget.attrs['placeholder'] = ''
        self.fields['records_file'].help_text = ''