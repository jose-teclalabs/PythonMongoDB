from django.conf.urls import patterns, include, url
from django.conf import settings
from LJblog.views import PostListView,goIndex

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(), name='list'),
    url(r'^post/', include('LJblog.urls')),
    url(r'^index/', goIndex, name='index'),
)


