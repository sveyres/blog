from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^post/list$', post_list),
    url(r'^post/(?P<p_id>\d+)/$', post_details)
]
