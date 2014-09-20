from django.conf.urls import patterns, url
from views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView,goServices,goPost
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^add/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[\w\d]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[\w\d]+)/edit/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[\w\d]+)/delete/$', PostDeleteView.as_view(), name='delete'),
    url(r'^post/list$',views.post_list,name='post_list'),
    url(r'^post/guardar$',views.guardar_post,name='guardar_post'),
    url(r'^Services$',views.goServices, name='mostrar'),
    url(r'^Google$',views.goapiGoogle, name='goapiGoogle'),
    url(r'^Post$',views.goPost, name='goPost'),
    url(r'^Hostoria$',views.goHistoria, name='goHistoria'),
    url(r'^Gallery$',views.goGallery, name='goGallery')

)

urlpatterns = format_suffix_patterns(urlpatterns)