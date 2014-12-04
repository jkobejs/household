"""
Moudle that contains views for graph application
"""
from django.views.generic import TemplateView

from transaction.models import Transaction
from common.utils import LoginRequiredMixin


class GraphsIndexView(LoginRequiredMixin, TemplateView):
    """
    Main graph view that shows graphs for monthly amount and yearly water and
    electricity expenditure.
    """
    template_name = 'graphs/index.html'

    def get_context_data(self, **kwargs):
        graph_data, amount = Transaction.objects.daily_amounts(self.request.user.household)
        context = super(GraphsIndexView, self).get_context_data(**kwargs)
        context['graph_data'] = graph_data
        context['amount'] = amount
        return context
