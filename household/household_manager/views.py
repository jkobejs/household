"""
Views module for household manager that provides views for creating and updating household,
also it provies views for creating and updating household members.
"""
from django.views.generic import CreateView, TemplateView, UpdateView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy

from .forms import HouseholdManagerForm
from household_member.forms import HouseholdMemberForm
from household.models import Household
from accounts.models import HouseholdUser
from common.utils import LoginRequiredMixin


class CreateManagerView(CreateView):
    """
    View clas that provides form for creating new Household manager.
    """
    form_class = HouseholdManagerForm
    success_url = "/"
    template_name = "household_manager/householdmanager_form.html"


class CreateHouseholdView(LoginRequiredMixin, CreateView):
    """
    View class that provides form for creating new Household instance.
    """
    success_url = reverse_lazy('household_manager_index')
    model = Household

    def form_valid(self, form):
        form.save()
        HouseholdUser.objects.filter(id=self.request.user.id).update(household=form.instance)
        return super(CreateHouseholdView, self).form_valid(form)


class UpdateHouseholdView(LoginRequiredMixin, UpdateView):
    """
    View class that provides form for updating Household instance.
    """
    success_url = reverse_lazy('household_manager_index')
    model = Household

    def get_context_data(self, **kwargs):
        context = super(UpdateHouseholdView, self).get_context_data(**kwargs)
        context['update'] = True
        return context


class CreateMemberView(LoginRequiredMixin, CreateView):
    """
    View class that provides form for creating new Household member.
    """
    success_url = reverse_lazy('household_manager_index')
    form_class = HouseholdMemberForm
    template_name = "household_manager/householdmember_form.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.household = self.request.user.household
        user.save()
        return super(CreateMemberView, self).form_valid(form)


class UpdateMemberView(LoginRequiredMixin, UpdateView):
    """
    View class that provides form for updating Household member.
    """
    form_class = HouseholdMemberForm
    model = HouseholdUser
    success_url = reverse_lazy('household_manager_index')
    template_name = "household_manager/householdmember_form.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateMemberView, self).get_context_data(**kwargs)
        context['update'] = True
        return context


class ManagerIndexView(LoginRequiredMixin, TemplateView):
    """
    View class that displays household instance and houehold members.
    """
    template_name = "household_manager/index.html"

    def get_context_data(self, **kwargs):
        context = super(ManagerIndexView, self).get_context_data(**kwargs)
        context['household'] = self.request.user.household
        context['household_members'] = HouseholdUser.objects.filter(
            ~Q(id=self.request.user.id),
            household=self.request.user.household
        ).values('id', 'first_name', 'last_name', 'email') if self.request.user.household else None
        return context
