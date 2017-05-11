from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^post/list$', post_list, name="post-list"),
    url(r'^post/(?P<p_slug>[\w-]+)/$', post_details, name="post-details")
]
