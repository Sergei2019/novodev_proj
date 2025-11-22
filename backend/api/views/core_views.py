from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import AnnouncementFilter, EventFilter

from core.models import News, Announcement, Event, MapPoint, Tag
from ..serializers.core_serializers import (NewsSerializer, 
                                            AnnouncementSerializer, 
                                            EventSerializer, 
                                            MapPointSerializer,
                                            TagSerializer)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AnnouncementFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = EventFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']


class MapPointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MapPoint.objects.all()
    serializer_class = MapPointSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None