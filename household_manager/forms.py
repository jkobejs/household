from accounts.forms import HouseholdUserForm


class HouseholdManagerForm(HouseholdUserForm):

    def __init__(self, *args, **kwargs):
        super(HouseholdManagerForm, self).__init__(*args, **kwargs)
        self.user_type = "manager"
