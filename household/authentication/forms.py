"""
Module that contains form for user authentication.
"""
from django import forms

from accounts.models import HouseholdUser


class LoginForm(forms.Form):
    """
    Form that authenticates user.
    """
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def __init__(self, *args, **kwargs):
        """
        Adds 'form-control' class and 'placeholder' to form field.
        """
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name.title()

    def clean(self):
        """
        Validates if username and password are valid.
        """
        cleaned = super(LoginForm, self).clean()

        if not cleaned.get('username'):
            self._errors['username'] = "Username or password cannot be blank."
            return cleaned

        if not cleaned.get('password'):
            self._errors['password'] = "Username or password cannot be blank."
            return cleaned

        try:
            user = HouseholdUser.objects.get(username=cleaned['username'])
            if not user.check_password(cleaned.get('password', '')):
                self._errors['password'] = "Wrong password for username: %s" % self.cleaned_data['username']
                return cleaned
        except HouseholdUser.DoesNotExist:
            self._errors['username'] = "User with specified username doesn't exists."
            return cleaned

        return self.cleaned_data
