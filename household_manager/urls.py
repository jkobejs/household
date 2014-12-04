"""
Module that defines url routes for household manager application.
"""
from django.conf.urls import patterns, url

from .views import CreateManagerView, CreateHouseholdView, UpdateHouseholdView, ManagerIndexView, CreateMemberView, \
    UpdateMemberView


urlpatterns = \
    patterns('',
             url(r'^$', view=ManagerIndexView.as_view(), name='household_manager_index'),
             url(r'^sign_up/$', view=CreateManagerView.as_view(), name='sign_up'),
             url(r'^household/$', view=CreateHouseholdView.as_view(), name='create_household'),
             url(r'^household/(?P<pk>\d+)/$', view=UpdateHouseholdView.as_view(), name='update_household'),
             url(r'^member/$', view=CreateMemberView.as_view(), name='create_member'),
             url(r'^member/(?P<pk>\d+)/$', view=UpdateMemberView.as_view(), name='update_member'),)
