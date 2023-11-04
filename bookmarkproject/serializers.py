from .models import Task
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'complete', 'created' ]