from django.conf.urls import url
from . import views
app_name = 'api'

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='list'),
    url(r'^create/$', views.PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', views.PostDestroyAPIView.as_view(), name='detele'),
]
