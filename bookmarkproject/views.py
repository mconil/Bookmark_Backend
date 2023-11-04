from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookmarkSerializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.AllowAny]
