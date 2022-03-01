from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
import re


class SignupForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'you_are_a']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('The given email is already registered')
        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters'


class SellProductForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Sell
        fields = ['product_name', 'category', 'price', 'location', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(SellProductForm, self).__init__(*args, **kwargs)
        # self.fields['image'].error_messages.update({'required': 'This field is required'})
        # self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ArticleForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].help_text = 'Your name or the name of the person writing the article'
        self.fields['block_quote'].help_text = 'A small quotation about your article preferably one to two sentences'
        self.fields['image'].help_text = 'Preferred image size : 840px width x 420px height'


class ImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ArticleImage
        fields = ['image']


class ProductImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ProductImage
        fields = '__all__'
        exclude = ['name']

