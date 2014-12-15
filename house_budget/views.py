"""
Contains views for main household page.
"""
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login

from authentication.forms import LoginForm


class HomeView(FormView):
    """
    Display home page and login form if user is not logged in.
    """
    template_name = "index.html"
    form_class = LoginForm
    success_url = reverse_lazy('transactions_index')

    def form_valid(self, form):
        """
        Logs in user if form is valid.
        """
        login(self.request, authenticate(**form.cleaned_data))
        return super(HomeView, self).form_valid(form)
