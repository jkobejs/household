"""
Contains TransactionForm model form that provides extra transaction type
field.
"""
from django.forms import ModelForm, ChoiceField, ValidationError

from transaction.models import Transaction


class TransactionForm(ModelForm):
    TRANSACTION_TYPE = (
        (True, "Add money"),
        (False, "Withdraw money")
    )
    transaction_type = ChoiceField(choices=TRANSACTION_TYPE)

    def clean(self):
        """
        Checks if amount is positive number and coverts in to negative if
        transaction type is withdraw money.
        """
        cleaned = self.cleaned_data

        if cleaned['transaction_type'] == "False":
            cleaned['amount'] = -self.cleaned_data['amount']

        return cleaned

    def clean_amount(self):
        """
        Raises ValidationError if amount is negative number.
        """
        if self.cleaned_data['amount'] < 0:
            raise ValidationError('Amount must be positive number, if you are withdrawing money '
                                  'please select appropriate transaction type.')

    class Meta(object):
        model = Transaction
        fields = ['description', 'amount', 'transaction_type']
