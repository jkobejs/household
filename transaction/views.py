"""
Module that contains main view for transactions which display transactions, household and users.
"""
from django.views.generic import CreateView

from .models import Transaction
from .forms import TransactionForm
from household_manager.views import LoginRequiredMixin
from accounts.models import HouseholdUser
from common.utils import get_paginated_page


class TransactionIndex(LoginRequiredMixin, CreateView):
    """
    View class that provides form for creation of transactions, displays previous transactions, household and
    all members of that transaction.
    """
    template_name = "transaction/index.html"
    form_class = TransactionForm
    success_url = '/transaction/'

    def form_valid(self, form):
        """
        Called when form is valid. Saves current user and its household in transaction.
        """
        transaction = form.save(commit=False)
        transaction.household = self.request.user.household
        transaction.household_user = self.request.user
        transaction.save()
        return super(TransactionIndex, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds data to context so that we can access it inside templates.
        """
        transactions_list = list(Transaction.get_transactions_from_household(self.request.user.household))
        context = super(TransactionIndex, self).get_context_data(**kwargs)
        context['household_members'] = HouseholdUser.get_users_from_household(self.request.user.household)
        context['transactions'] = get_paginated_page(transactions_list, self.request.GET.get('page'))
        context['amount'] = Transaction.calculate_amount(transactions_list)
        context['household'] = self.request.user.household

        return context
