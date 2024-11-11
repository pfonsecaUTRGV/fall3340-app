from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'somethin@domain.com'}))
	first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}))
	last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your last name'}))