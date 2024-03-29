from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^publishing/$', views.publishing_list,name='publishing_list'),  # r是正则表达式中不转义的意思
    # url(r'^add_publishing/$', views.add_publishing),
    # 在django1.1中用url，在django2.0中用path或re_path，其中re_path的用法和1.1中的url是一样的
    re_path(r'^add_publishing/$', views.AddPublishing.as_view(),name='add_publishing'),
    re_path(r'^edit_publishing/', views.edit_publishing),
    url(r'delete_(?P<table>publishing|book|author)/(?P<delete_id>\d+)$',views.delete,name='delete'),
    # <a class="btn btn-danger" href="/app01/delete_publishing/14">删除</a>
    # url(r'^delete_publishing/(?P<delete_id>\d+)$', views.delete_publishing,name='delete_publishing'),  # (?P<delete_id>\d+)命名分组
    # url(r'^delete_publishing/(\d+)$', views.delete_publishing),  # # (\d+)分组
    url(r'^book/$',views.book_list,name='book_list'),
    url(r'^add_book/$',views.add_book),
    url(r'^edit_book/$',views.edit_book),
    # url(r'^delete_book/$',views.delete_book),
    url(r'^author_list/$',views.author_list,name='author_list'),
    url(r'^add_author/$',views.add_author),
    # url(r'^delete_author/$',views.delete_author),
    url(r'^edit_author/$',views.edit_author),
]
