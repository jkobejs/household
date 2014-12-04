"""
Module that contains models for Transaction application.
"""
from django.db import models

from .managers import TransactionManager
from accounts.models import HouseholdUser


class Transaction(models.Model):
    """
    Model that represents money transaction created by specific user. It contains
    date when transaction was made, amount of money that was spent, user that
    created it an type of transaction.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    household_user = models.ForeignKey(HouseholdUser, default=None)

    objects = TransactionManager()

    class Meta(object):
        ordering = ['-date_created']

    @staticmethod
    def calculate_amount(transactions_list):
        """
        Returns total sum of amounts for transactions in given list.
        """
        return sum([transaction['amount'] for transaction in transactions_list])

    @classmethod
    def get_transactions_from_household(cls, household):
        """
        Returns values queryset for transactions from given household.
        """
        return cls.objects.filter(household_user__household=household).select_related('household_user').\
            values('description', 'household_user__first_name', 'date_created',
                   'household_user__last_name', 'amount')
