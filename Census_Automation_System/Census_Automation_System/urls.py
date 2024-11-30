"""
URL configuration for Census_Automation_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import debug_toolbar
from django.urls import include, path
from census import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path("", views.homePage, name='homePage'),
    path("About/", views.aboutUs, name='aboutUs'),
    path("CensusPage/", views.censusPage, name='censusPage'),
    path("ContactSubmit/", views.contactSubmit, name='contactSubmit'),
    path("Contact/", views.contact, name='contact'),
    path("FAQs/", views.faqs, name='faqs'),
    path("ForgotPassword/", views.forgotPassword, name='forgotPassword'),
    path("Help/", views.help, name='help'),
    path("LogIn/", views.logIn, name='logIn'),
    path("ResetPassword/", views.resetPassword, name='resetPassword'),
    path("SignUp/", views.signUp, name='signUp'),
    path("Success/", views.success, name='success'),
    path("LogOut/", views.logOut, name='logOut'),
    path('census/', include('census.urls')),  # Ensure this line is present
]