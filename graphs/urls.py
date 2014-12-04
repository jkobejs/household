"""
Contains urls for graph application.
"""
from django.conf.urls import patterns, url
from .views import GraphsIndexView

urlpatterns = patterns('',
                       url(r'^$', GraphsIndexView.as_view(), name='graphs_index'))
