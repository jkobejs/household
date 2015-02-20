"""
Module that contains forms that are related to main user model.
"""
from django import forms

from django.contrib.auth import get_user_model


class HouseholdUserForm(forms.ModelForm):
    """
    Provides user creation and modification.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(object):
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "email"]

    def __init__(self, *args, **kwargs):
        """
        Adds 'form-control' class and 'placeholder' to form field.
        """
        super(HouseholdUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.CharField):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field_name.title()

    def save(self, commit=True, **kwargs):
        """
        Saves user data, sets its password and type.
        """
        instance = super(HouseholdUserForm, self).save(commit=False, **kwargs)
        instance.set_password(self.cleaned_data["password"])
        if commit:
            instance.user_type = self.user_type
            instance.save()
            self.group.user_set.add(instance)

        return instance
