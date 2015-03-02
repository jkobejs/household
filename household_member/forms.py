from accounts.forms import HouseholdUserForm


class HouseholdMemberForm(HouseholdUserForm):

    def __init__(self, *args, **kwargs):
        super(HouseholdMemberForm, self).__init__(*args, **kwargs)
        self.user_type = "member"
        