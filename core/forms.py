from django import forms
from .models import PersonalDetail, AddressDetail
from django.forms import Select, RadioSelect

class DateInput(forms.DateInput):
    input_type = 'date'

class Form1(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        widgets = {
            'dob':DateInput(),
            'gender':Select(),
            'b_group':Select(),
            'citizenship_issue_district':Select(),
            'w_relationship':Select(),
        }
        fields ='__all__'

class  Form2(forms.ModelForm):
    class Meta:
        model = AddressDetail
        widgets = {
            'zone':Select(),
            'district':Select(),
            'l_issue_office':Select(),
            'l_category':RadioSelect(),
            's_zone':Select(),
        }
        exclude = ('p_detail',)
        fields ='__all__'