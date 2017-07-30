from django.conf.urls import url
from .views import posts_detail, PostList


urlpatterns = [
    # url(r'^$', posts_list, name='home'),
    url(r'^$', PostList.as_view(), name='home'),
    url(r'category/(?P<category_slug>[\w\d-]+)/$', PostList.as_view(), name='in_category'),
    # url(r'(?P<pk>\d+)/$', posts_create, name='create'),
    url(r'(?P<slug>[\w\d-]+)/$', posts_detail, name='detail'),
    # url(r'(?P<pk>\d+)/$', posts_update, name='update'),
    # url(r'(?P<pk>\d+)/$', posts_delete, name='delete'),
]
