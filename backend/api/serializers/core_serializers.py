from rest_framework import serializers

from core.models import (News, 
                         Announcement,
                         Event,
                         MapPoint,
                         Tag,
                         Post,
                         Topic,
                         NewsCategory,
                         Gallery,
                         FeedBack,
                         Attractions,
                         AttractionImage,
                         Organization,
                         Vacancy)
from ..serializers.user_serializers import UserSerializer


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class MapPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    topic_title = serializers.CharField(source='topic.title', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'topic_title']

class TopicSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post_count = serializers.IntegerField(source='posts.count', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ['author']

class AttractionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionImage
        fields = ['id', 'image', 'order']

class AttractionsSerializer(serializers.ModelSerializer):
    images = AttractionImageSerializer(many=True, read_only=True)

    class Meta:
        model = Attractions
        fields = '__all__'