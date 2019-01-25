from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>\d+)$', views.post_detail, name='detaill'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
]
