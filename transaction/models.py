"""
Module that contains models for Transaction application.
"""
from itertools import groupby

from django.db import models

from .managers import TransactionManager
from accounts.models import HouseholdUser
from common.utils import get_number_of_days_in_current_month


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

    # Todo: remove if not needed
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

    @classmethod
    def daily_amounts(cls, household, step=5):
        """
        Returns tuple that contains list of aggregated amounts and total amount in
        current month for specified household.
        """
        month, number_of_days = get_number_of_days_in_current_month()

        grouped = groupby(
            cls.objects.filter(household_user__household=household, date_created__month=month).values(
                'date_created',
                'amount'
            ),
            lambda x: x['date_created'].day
        )

        daily_amounts = {day: sum([item['amount'] for item in group]) for day, group in grouped}

        amounts = [int(daily_amounts.get(index, 0)) for index in xrange(number_of_days)]

        result = [amounts[0]] + [sum(amounts[index:index + step]) for index in xrange(1, number_of_days, step)]

        amount = 0
        for i, val in enumerate(result):
            amount += val
            result[i] = amount

        return result, amount
