from rest_framework import serializers
from core.models import Topic, Post
from .user_serializers import UserSerializer

class TopicSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post_count = serializers.IntegerField(source='posts.count', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ['author']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    topic_title = serializers.CharField(source='topic.title', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'topic_title']