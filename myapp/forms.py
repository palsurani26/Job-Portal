# forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import ApplyJobApplication, Job


class UploadFileForm(forms.Form):
    file = forms.FileField()
class UserSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
class OTPVerificationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    otp_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the OTP'}))

class PasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.HiddenInput())  # Hidden field to pass the email
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}))

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')  # Add or remove fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False  # Optionally allow password update


        from django import forms

# Assuming you have a model for JobApplication (we'll create this next)
class JobApplicationForm(forms.Form):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    # Education Details
    highest_qualification = forms.ChoiceField(
        choices=[
            ('Doctorate/PhD', 'Doctorate/PhD'),
            ('Masters/Post-Graduation', 'Masters/Post-Graduation'),
            ('Graduation/Diploma', 'Graduation/Diploma'),
            ('12th', '12th'),
            ('10th', '10th'),
            ('Below 10th', 'Below 10th')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    course_specialization = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Course and Specialization'}))
    
    # Past Experience
    experience = forms.ChoiceField(
        choices=[
            ('none', 'None'),
            ('1-5', '1-5 years'),
            ('5-10', '5-10 years'),
            ('10+', '10 and above')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Company Name'}), required=False)
    
    # CV Upload
    cv = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

class JobForm(forms.ModelForm):
    last_date_to_apply = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Last Date to Apply"
    )

    class Meta:
        model = Job
        fields = [
            'title', 
            'company_name', 
            'location', 
            'job_type', 
            'description', 
            'who_can_apply', 
            'last_date_to_apply'
        ]
        from django import forms
from .models import JobApplication

class JobApplicationFormm(forms.ModelForm):
    class Meta:
        model = ApplyJobApplication
        fields = ['firstname', 'lastname', 'email', 'company', 'location', 'job_type', 'job_description', 'cv']  # Adjust fields based on your model

    cv = forms.FileField(required=True)  # File upload for CV

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].widget.attrs['readonly'] = True
        self.fields['location'].widget.attrs['readonly'] = True
        self.fields['job_type'].widget.attrs['readonly'] = True
        self.fields['job_description'].widget.attrs['readonly'] = True


    