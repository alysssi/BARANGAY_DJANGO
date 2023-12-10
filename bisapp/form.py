from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import UserProfile
from .models import DocumentRequest
from .models import IncidentReport


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name' ,'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'middle_name', 'extension', 'birthdate', 'phone_number', 'email', 'address', 'gender']





class DocumentRequestForm(forms.ModelForm):
    class Meta:
        model = DocumentRequest
        fields = ['document_type', 'delivery_date', 'payment_type', 'purpose']





class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['resident_name','incident_date', 'incident_type', 'description',]


