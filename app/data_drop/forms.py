from django import forms
from .models import Dataset

PERSONAL_DATA_CHOICES = [
    ('basic','Basic Personal Data'),
    ('personal','Personal Data'),
    ('sensitive','Sensitive Personal Data')
    ]

EXPORT_CONTROL_CHOICES = [
    ('not_technical','Not Technical'),
    ('not_listed','Not Listed'),
    ('not_assessed','Not Assessed'),
    ('dual_use','Dual Use'),
    ('military/assimilated','Military/Assimilated'),
]

NATIONAL_SECURITY_CHOICES = [
    ('national_security','National Security'),
    ('not_national_security','Not National Security'),
]

COMPANY_SENSITIVE_CHOICES = [
    ('navblue_amber','Navblue AMBER'),
    ('navblue_red','Navblue RED'),
    ('not_applicable','Not Applicable'), 
]
BUSINESS_PRIVATE_CHOICES = [
    ('business_data','Business Data'),
    ('private_data','Private Data'),
]
class DatasetForm(forms.ModelForm):
    dataset = forms.FileField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-detail'}))
    personal_data = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-detail'}),
        choices=PERSONAL_DATA_CHOICES)
    export_control = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-detail'}),
        choices=EXPORT_CONTROL_CHOICES)
    national_security = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-detail'}),
        choices=NATIONAL_SECURITY_CHOICES)
    company_sensitve = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-detail'}),
        choices=COMPANY_SENSITIVE_CHOICES)
    business_private = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-detail'}),
        choices=BUSINESS_PRIVATE_CHOICES)

    class Meta:
        model = Dataset
        fields = '__all__'
        
    