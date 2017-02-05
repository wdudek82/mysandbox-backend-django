from django.conf.urls import url
from .views import posts_detail, posts_home


urlpatterns = [
    url(r'(?P<pk>\d+)/', posts_detail, name='detail'),
    url(r'^$', posts_home, name='home')
]