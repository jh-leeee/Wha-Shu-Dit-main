"""project_WSD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from whashudit import views
from django.contrib.auth import views as auth_views

app_name = 'whashudit'

urlpatterns = [
    # http://localhost:8000/
    # path('', )
    # http://localhost:8000/login/
    path('login/', auth_views.LoginView.as_view(template_name='whashudit/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    # path('detail/',views.asdf, name='asdf')
    path('search/', views.search, name='search')
]


