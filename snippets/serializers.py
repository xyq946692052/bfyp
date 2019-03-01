from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, PicFile


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('id', 'url', 'created', 'updated', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet-detail',
        read_only=True)

    pics = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='pic-detail',
        read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets', 'pics')


class PicSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PicFile
        fields = ('id', 'url', 'created', 'updated', 'owner', 'pic')

