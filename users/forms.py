from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

#User Registration and validation
class UserRegisterForm(UserCreationForm):
    """Collect registration details using Django's user-creation validation."""
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#User Updating info on profiles page
#Widgets defining how form fields rendered in HTML bootstrap

class UserUpdateForm(forms.ModelForm):
    """Allow a user to update their personal details and email address."""
    email = forms.EmailField(  
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control"})
)

    class Meta: 
        model = User
        fields = ["first_name", "last_name", "email"]


        widgets = {
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),

        }

#Ensuring emails are unique, rejects email addresses already assigned to another user

    def clean_email(self):
        """Reject email addresses already assigned to another user."""
        email= self.cleaned_data["email"]

        if (User.objects
        .filter(email__iexact=email)
        .exclude(pk=self.instance.pk)
        .exists()
        ):
            raise forms.ValidationError(
                "An account with this email address already exists."
            )

        return email

#Additional profile info form, allows the user to update their phone number and department.

class ProfileUpdateForm(forms.ModelForm):
    """Allow a user to update their phone number and department."""
    class Meta: 
        model= Profile
        fields = ["phone", "department"]

        widgets = {
            "phone": forms.TextInput(attrs={"class":"form-control"}),
            "department": forms.TextInput(attrs={"class":"form-control"}),

        }