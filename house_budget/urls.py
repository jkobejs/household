"""
Contains urls that maps to urls of all application inside the project.
"""
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from .views import HomeView
from authentication.views import logout_view


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name="home"),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^household_manager/', include('household_manager.urls')),
                       url(r'^logout/', view=logout_view, name="logout"),
                       url(r'^transaction/', include("transaction.urls")),
                       url(r'^graphs/', include("graphs.urls")),)

urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)