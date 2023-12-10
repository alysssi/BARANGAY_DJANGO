"""
URL configuration for BIS project.

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


from bisapp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bisapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('Signup/', views.SignUp, name = 'signup'),
    path('Signin/', views.signin, name = 'signin'),
    path('contact/', views.contact, name = 'contact'),
    path('Events/', views.events, name = 'events'),
    path('About/', views.about, name = 'about'),
    path('Main/', views.main, name = 'main'),
    path('profileform/', views.profile_form, name='profileform'),
    path('request/', views.request, name='request'),
    path('request_history/', views.request_history, name='request_history'),
    path('report/', views.report, name='report'),
    path('report_history/', views.report_history, name='report_history'),
    path('adminUI/', views.adminUI, name='adminUI'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_users/', views.admin_users, name='admin_users'),
    path('admin_users_request/', views.admin_users_request, name='admin_users_request'),
    path('admin_users_report/', views.admin_users_report, name='admin_users_report'),
    path('admin_message/', views.message, name='message'),
    path('forget/', views.forget, name='forget'),
    path('profile/', views.profile, name='profile'),
    
    
    
    
    path('logout/', views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
