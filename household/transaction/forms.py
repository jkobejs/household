"""
Contains TransactionForm model form that provides extra transaction type
field.
"""
from django.forms import ModelForm, ChoiceField, ValidationError

from transaction.models import Transaction


class TransactionForm(ModelForm):
    """
    Form for adding new transactions.
    """
    TRANSACTION_TYPE = (
        (True, "Add money"),
        (False, "Withdraw money")
    )
    transaction_type = ChoiceField(choices=TRANSACTION_TYPE)

    def __init__(self, *args, **kwargs):
        """
        Adds 'form-control' class and 'placeholder' to form field.
        """
        super(TransactionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name.title()

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
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise ValidationError('Amount must be positive number, if you are withdrawing money '
                                  'please select appropriate transaction type.')
        return amount

    class Meta(object):
        model = Transaction
        fields = ['description', 'amount', 'transaction_type']
