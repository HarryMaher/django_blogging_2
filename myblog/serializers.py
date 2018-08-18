from django.contrib.auth.models import User, Group
from myblog.models import Post, Category
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'published_date')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'posts')