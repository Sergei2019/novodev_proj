from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'news', views.NewsViewSet)
router.register(r'announcements', views.AnnouncementViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'map-points', views.MapPointViewSet)
router.register(r'forum-topics', views.ForumTopicViewSet)
router.register(r'forum-posts', views.ForumPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]