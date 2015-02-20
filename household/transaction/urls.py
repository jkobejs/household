__author__ = 'jgrgurica'
from django.conf.urls import patterns, url
from .views import TransactionIndex

urlpatterns = patterns('',
        url(r'^$', TransactionIndex.as_view(), name='transactions_index'))