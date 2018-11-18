"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

from blog import views
from django.contrib.auth.views import ( 
	PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView, 
)
from blog.backends import MyRegistrationView


urlpatterns = [

path('', views.index, name='home'),
path('about/', TemplateView.as_view(template_name='about.html'), name='about'), 
path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
path('entries/', RedirectView.as_view(pattern_name='browse', permanent=True)),
path('entries/<slug>/', views.entry_detail, name='entry_detail'),
path('entries/<slug>/edit/', views.edit_entry, name='edit_entry'),
path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
path('browse/name/', views.browse_by_name, name='browse'),
path('browse/name/<initial>/', views.browse_by_name, name='browse_by_name'),
path('accounts/password/reset/', PasswordResetView.as_view (template_name='registration/password_reset_form.html'), name="password_reset"),
path('accounts/password/reset/done/', PasswordResetDoneView.as_view (template_name='registration/password_reset_done.html'), name="password_reset_done"),
path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
name="password_reset_complete"),
path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
path('accounts/create_entry/', views.create_entry, name='registration_create_entry'),
path('accounts/', include('registration.backends.simple.urls')),
path('admin/', admin.site.urls), 
# path('accounts/create_entry/', CreateEntryView.as_view (template_name='entries_create_entry.html'), name='registration_create_entry'),
]



