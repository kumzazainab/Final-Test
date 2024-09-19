from django import forms
from .models import Income, Expenses
from django.contrib.auth.forms import  AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control','data-toggle': 'password','id': 'password','name': 'password',}))
    remember_me = forms.BooleanField(required=False)

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount']

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['amount']
