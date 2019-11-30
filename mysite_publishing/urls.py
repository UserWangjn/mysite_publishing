"""mysite_publishing URL Configuration

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
from django.conf.urls import url
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^publishing_list/$', views.publishing_list),
    url(r'^add_publishing/$', views.add_publishing),
    url(r'^edit_publishing/$', views.edit_publishing),
    url(r'^delete_publishing/$', views.delete_publishing),
    url(r'^book_list/$',views.book_list),
    url(r'^add_book/$',views.add_book),
    url(r'^edit_book/$',views.edit_book),
    url(r'^delete_book/$',views.delete_book),
    url(r'^author_list/$',views.author_list),
    url(r'^add_author/$',views.add_author),
    url(r'^delete_author/$',views.delete_author),
    url(r'^edit_author/$',views.edit_author),
]
