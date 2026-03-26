"""
URL configuration for stockex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from APP import views

admin.site.site_header = "TradePur Adminstrator"
admin.site.site_title = "TradePur Admin Portal"
admin.site.index_title = "Welcome TradePur Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("otp/",views.otp_verify),
    path("login/",views.login_page),
    path("pin/",views.pin),
    path("logout/",views.logout,name='logout'),
    path("dashboard/",views.dashboard),
    path("dashboard_s/",views.dashboard_s),
    path("user/",views.user_profile,name="profile"),
    path("enter_email/",views.email_enter,name="enter_email"),
    
    path("tesla/",views.tesla,name='tesla'),
    path("microsoft/",views.microsoft,name='microsoft'),
    path("visa/",views.visa,name='visa'),
    path("unitedhealth/",views.unitedhealth,name='unitedhealth'),
    path("cocacola/",views.cocacola,name='cocacola'),
    path("chevron/",views.chevron,name='chevron'),
    path("cisco/",views.cisco,name='cisco'),
    path("intel/",views.intel,name='intel'),
    path("disney/",views.disney,name='disney'),
    path("jpmorgan/",views.jpmorgan,name='jpmorgan'),
    path("mastercard/",views.mastercard,name='mastercard'),
    path("adeia/",views.adeia,name='adeia'),
    path("albertsons/",views.albertsons,name='albertsons'),
    path("google/",views.google,name='google'),
    path("amazon/",views.amazon,name='amazon'),
    path("apple/",views.apple,name='apple'),

]
