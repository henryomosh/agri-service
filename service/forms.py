from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
import re


class SignupForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('The given email is already registered')
        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters'


class ServiceProviderForm(forms.ModelForm):

    class Meta:
        model = ServiceProvider
        fields = '__all__'


class SellProductForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'




