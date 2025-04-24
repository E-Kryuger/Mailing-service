"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path

from mailings.views.clients import (
    ClientCreateView,
    ClientListView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
)
from mailings.views.messages import (
    MessageCreateView,
    MessageListView,
    MessageDetailView,
    MessageUpdateView,
    MessageDeleteView,
)
from mailings.views.mailings import (
    MailingCreateView,
    MailingListView,
    MailingDetailView,
    MailingUpdateView,
    MailingDeleteView,
    MailingSendView,
    MailingScheduleView,
    MailingCancelView,
    MailingDisableView,
)
from mailings.views.statistics import (
    IndexView,
    MailingAttemptsView,
    UserAttemptsView,
)

__all__ = [
    ClientCreateView,
    ClientListView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    MessageCreateView,
    MessageListView,
    MessageDetailView,
    MessageUpdateView,
    MessageDeleteView,
    MailingCreateView,
    MailingListView,
    MailingDetailView,
    MailingUpdateView,
    MailingDeleteView,
    MailingSendView,
    MailingScheduleView,
    MailingCancelView,
    MailingDisableView,
    IndexView,
    MailingAttemptsView,
    UserAttemptsView,
]
from mailings.apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path("mailings-attempts/", UserAttemptsView.as_view(), name="user_attempts"),
    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/add/", ClientCreateView.as_view(), name="client_create"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("clients/<int:pk>/edit/", ClientUpdateView.as_view(), name="client_update"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("messages/", MessageListView.as_view(), name="message_list"),
    path("messages/add/", MessageCreateView.as_view(), name="message_create"),
    path("messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
    path("messages/<int:pk>/edit/", MessageUpdateView.as_view(), name="message_update"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("mailings/", MailingListView.as_view(), name="mailing_list"),
    path("mailings/add/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailings/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
    path("mailings/<int:pk>/edit/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailings/<int:pk>/disable/", MailingDisableView.as_view(), name="mailing_disable"),
    path("mailings/<int:pk>/schedule/", MailingScheduleView.as_view(), name="mailing_schedule"),
    path("mailings/<int:pk>/cancel/", MailingCancelView.as_view(), name="mailing_cancel"),
    path("mailings/<int:pk>/attempts/", MailingAttemptsView.as_view(), name="mailing_attempts"),
    path("mailings/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailings/<int:pk>/send/", MailingSendView.as_view(), name="mailing_send"),
]
