from django.db import models
from users.models import User


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название рубрики")

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"

    def __str__(self):
        return self.name
    
class EventCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория мероприятия")

    class Meta:
        verbose_name = "Категория мероприятия"
        verbose_name_plural = "Категории мероприятия"

    def __str__(self):
        return self.name



class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новости")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Фото")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Теги")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    short_description = models.CharField(verbose_name="Текст новости")
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Рубрика")
    top = models.BooleanField(default=False, verbose_name='топовые новости')


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    

class NewsComment(models.Model):
    news = models.ForeignKey('News', related_name='comments', on_delete=models.CASCADE, verbose_name="Новость")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    content = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата комментария")

    class Meta:
        verbose_name = "Комментарий к новости"
        verbose_name_plural = "Комментарии к новости"
        ordering = ['created_at']

    def __str__(self):
        return f"Комментарий от {self.author.username} к '{self.news.title}'"

    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name
    

class Announcement(models.Model):
    CATEGORY_CHOICES = [
        ('sale', 'Продажа'),
        ('buy', 'Покупка'),
        ('service', 'Услуга'),
        ('other', 'Другое'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Цена")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='other', verbose_name="Категория")
    image = models.ImageField(upload_to='announcements/', blank=True, null=True, verbose_name="Фото")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} от {self.user.username}"
    

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    description = models.TextField(verbose_name="Описание")
    date_time = models.DateTimeField(verbose_name="Дата и время")
    location = models.CharField(max_length=255, verbose_name="Место проведения")
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория мероприятия")
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['date_time']

    def __str__(self):
        return self.title


class Organization(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название организации")
    price = models.FloatField()
    grafik_raboty = models.TextField(verbose_name="График работы")
    description = models.TextField(verbose_name="Описание")
    phone_number = models.CharField(verbose_name="Телефон")

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ['title']

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    price = models.IntegerField()
    grafik_raboty = models.TextField(verbose_name="График работы")
    description = models.TextField(verbose_name="Описание")
    phone_number = models.CharField(verbose_name="Телефон")
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансия"
        ordering = ['title']

    def __str__(self):
        return self.title


class MapPoint(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")
    category = models.CharField(max_length=100, blank=True, verbose_name="Категория (школа, магазин и т.п.)")
    image = models.ImageField(upload_to='map_points/', blank=True, null=True, verbose_name="Фото")
    type = models.CharField(default=None, verbose_name="тип")

    class Meta:
        verbose_name = "Точка на карте"
        verbose_name_plural = "Точки на карте"

    def __str__(self):
        return self.title


class Attractions(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Полное описание")
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")
    short_description = models.TextField(blank=True, verbose_name="Краткое описание")

    class Meta:
        verbose_name = "Достопримечательность"
        verbose_name_plural = "Достопримечательности"

    def __str__(self):
        return self.title

class AttractionImage(models.Model):
    attraction = models.ForeignKey(Attractions, related_name='images', on_delete=models.CASCADE, verbose_name="Достопримечательность")
    image = models.ImageField(upload_to='attractions/', verbose_name="Фото")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок") 

    class Meta:
        verbose_name = "Изображение достопримечательности"
        verbose_name_plural = "Изображения достопримечательностей"
        ordering = ['order'] 

    def __str__(self):
        return f"Фото для {self.attraction.title}"