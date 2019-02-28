from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from snippets.permissions import IsOwnerOrReadOnly
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """此视图自动提供list, create, retrieve, update,destory操作"""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """此视图自动提供list和detail操作"""
    queryset = User.objects.all()
    serializer_class = UserSerializer



