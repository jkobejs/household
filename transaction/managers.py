"""
Module that provides managers for Transaction model.
"""
from itertools import groupby

from django.db import models

from common.utils import get_number_of_days_in_current_month


class TransactionManager(models.Manager):
    """
    Manager that provides some specific methods for retrieving transactions data.
    """
    # Todo: remove from managers, it is model method.
    def daily_amounts(self, household):
        """
        Returns tuple that contains list of aggregated amounts and total amount in
        current month for specified household.
        """
        month, number_of_days = get_number_of_days_in_current_month()

        grouped = groupby(
            self.filter(household_user__household=household, date_created__month=month).values(
                'date_created',
                'amount'
            ),
            lambda x: x['date_created'].day
        )

        daily_amounts = {day: sum([item['amount'] for item in group]) for day, group in grouped}

        amounts = [int(daily_amounts.get(index, 0)) for index in xrange(number_of_days)]

        step = 5

        result = [amounts[0]] + [sum(amounts[index:index + step]) for index in xrange(1, number_of_days, step)]
        amount = 0
        for i, val in enumerate(result):
            amount += val
            result[i] = amount
        return result, amount
