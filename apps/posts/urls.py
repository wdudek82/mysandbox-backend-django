from django.conf.urls import url
from .views import post_create, posts_detail, posts_list, post_update, post_delete


urlpatterns = [
    url(r'^$', posts_list, name='home'),
    # url(r'(?P<pk>\d+)/$', posts_create, name='create'),
    url(r'(?P<pk>\d+)/$', posts_detail, name='detail'),
    # url(r'(?P<pk>\d+)/$', posts_update, name='update'),
    # url(r'(?P<pk>\d+)/$', posts_delete, name='delete'),
]
