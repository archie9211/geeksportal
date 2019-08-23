"""geeksportal_website URL Configuration

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
from django.urls import path, include
from main.views import IndexPageView, ChangeLanguageView, HomePageView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('subs/', ProfileView.as_view(), name='profile'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('', include('tutorials.urls'), name='tutorial'),
    path('home/', HomePageView.as_view(), name='home'),
    path('index/', IndexPageView.as_view(), name='index'),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
    path('home/forum/post/<int:post_id>', HomePageView.as_view(), name='post_reply'),
]
