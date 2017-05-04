from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^post/list', post_list)
]
