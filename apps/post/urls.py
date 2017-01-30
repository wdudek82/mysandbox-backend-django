from django.conf.urls import url
from .views import post_detail, home


urlpatterns = [
    url(r'(?P<pk>\d+)/', post_detail, name='detail'),
    url(r'^$', home, name='home')
]