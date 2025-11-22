import django_filters
from core.models.core_models import News, Announcement, Event
from django.db import models 

class NewsFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name='category__id')
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = News
        fields = ['category', 'start_date', 'end_date']

class EventFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    category_id = django_filters.NumberFilter(field_name='category__id')
    class Meta:
        model = Event
        fields = [
            # 'category_id' уже определён выше как ChoiceFilter
            # 'search' определён выше как CharFilter с методом
        ]

    def filter_search(self, queryset, name, value):
        """
        Кастомный метод для поиска по заголовку и описанию.
        """
        if value:
            return queryset.filter(
                models.Q(title__icontains=value) |
                models.Q(description__icontains=value)
            )
        return queryset


class AnnouncementFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    category_id = django_filters.ChoiceFilter(
        field_name='category', 
        choices=Announcement.CATEGORY_CHOICES, 
        label='Категория'
    )
    published_date_start = django_filters.DateFilter(field_name='created_at', lookup_expr='date__gte')
    published_date_end = django_filters.DateFilter(field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = Announcement
        fields = [ 'search', 'category_id', 'published_date_start', 'published_date_end']

    def filter_search(self, queryset, name, value):
        """
        Кастомный метод для поиска по заголовку и описанию.
        """
        if value:
            return queryset.filter(
                models.Q(title__icontains=value) |
                models.Q(description__icontains=value)
            )
        return queryset
    
