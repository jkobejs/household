__author__ = 'jgrgurica'
from django.contrib.auth.models import Group

from accounts.forms import HouseholdUserForm


household_member_group, created = Group.objects.get_or_create(name="Household_member")


class HouseholdMemberForm(HouseholdUserForm):

    def __init__(self, *args, **kwargs):
        super(HouseholdMemberForm, self).__init__(*args, **kwargs)
        self.user_type = "member"
        self.group = household_member_group