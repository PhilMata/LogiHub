from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class':"form-control"})


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].widget.attrs.update({'class':"form-control"})
