from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40,
                               label="Pet name")
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Secret code')
