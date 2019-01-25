from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'comment.api'

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='list'),
    url(r'^create/$', views.PostCreateAPIView.as_view(), name='create'),
]
