__author__ = 'jgrgurica'
from django.contrib.auth.models import Group

from accounts.forms import HouseholdUserForm


household_manager_group, created = Group.objects.get_or_create(name="Household_manager")


class HouseholdManagerForm(HouseholdUserForm):

    def __init__(self, *args, **kwargs):
        super(HouseholdManagerForm, self).__init__(*args, **kwargs)
        self.user_type = "manager"
        self.group = household_manager_group