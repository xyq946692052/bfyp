from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from snippets.views import SnippetViewSet, UserViewSet, PicViewSet
from snippets import views


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destory'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

pic_list = PicViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

pic_detail = PicViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destory'
})

urlpatterns = [
    path('snippets', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
    path('users', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
    path('pics', pic_list, name='pic-list'),
    path('pics/<int:pk>', pic_detail, name='pic-detail'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns = format_suffix_patterns(urlpatterns)