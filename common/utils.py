"""
Module that provides utility functions and classes for project.
"""
import calendar
import datetime

from django.utils.http import urlunquote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    """
    Mixin that provides method that checks if user is logged in.
    """
    @classmethod
    def as_view(cls, **initkwargs):
        """
        Checks if user is logged in.
        """
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def get_paginated_page(objects, page_number, limit=5):
    """
    Returns wanted paginated page from objects.
    """
    paginator = Paginator(objects, limit)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def get_number_of_days_in_current_month():
    """
    Returns tuple (month, number_of days) where month is current month
    and number_of_days is number of days in current month.
    """
    now = datetime.datetime.now()
    return (now.month, calendar.monthrange(now.year, now.month)[1])


def upload_to_callable(instance, filename):
    """
    Assigns filename to photo and return path.
    """
    return urlunquote(filename)
