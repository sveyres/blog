from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^post/list$', post_list, name="post-list"),
    url(r'^post/(?P<p_id>\d+)/$', post_details, name="post-details"),
    url(r'^post/(?P<p_slug>[\w-]+)/$', post_details_slug, name="post-details-slug")
]
