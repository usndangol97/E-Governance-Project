from django import forms
from django.db import models
from .models import Resume
from django.forms import RadioSelect

class DateInput(forms.DateInput):
    input_type = 'date'

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        # fields = ['name','surname','birthdate','gender','father','mother','birthplace']
        widgets = {'birthdate':DateInput(),
                'issue_date':DateInput(),
                'gender':RadioSelect()
        }  