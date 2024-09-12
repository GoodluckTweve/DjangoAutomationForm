from django import forms
from .models import IntermediaryCloudAccess
from .models import CCEmail 
from .models import CloudAccessEmail
from django.core.validators import RegexValidator, FileExtensionValidator


class IntermediaryCloudAccessForm(forms.ModelForm):
  
    mobile_number = forms.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
        max_length=15
    )
    tin_document = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        required=False
    )
    tira_cert = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        required=False
    )
    brela_document = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        required=False
    )
    vrn_document = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        required=False
    )

    class Meta:
        model = IntermediaryCloudAccess
        fields = [
            'broker_agent_name', 'tin_no', 'vrn_registered', 'vrn_no',
            'address', 'mobile_number', 'company_email',
            'tin_document', 'tira_cert', 'brela_document', 'vrn_document'
        ]
        widgets = {
            'vrn_registered': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'tin_document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'tira_cert': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'brela_document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'vrn_document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class CCEmailForm(forms.ModelForm):
    class Meta:
        model = CCEmail
        fields = ['cc_email']

class CloudAccessEmailForm(forms.ModelForm):
    class Meta:
        model = CloudAccessEmail
        fields = ['cloud_access_email']
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

def clean_email(self):
    email = self.cleaned_data.get('email')