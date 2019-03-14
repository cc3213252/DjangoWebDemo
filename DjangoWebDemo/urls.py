"""DjangoWebDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'StaffManage.views.index', name='StaffManage'),
    url(r'^add_user_info_list$','StaffManage.views.add_user_info_list', name='add_user_info_list'),
    url(r'^delete_user_info_list$','StaffManage.views.delete_user_info_list', name='delete_user_info_list'),
    url(r'^update_user_info_list$','StaffManage.views.update_user_info_list', name='update_user_info_list'),
    url(r'^get_user_info_list$','StaffManage.views.get_user_info_list', name='get_user_info_list'),
]
