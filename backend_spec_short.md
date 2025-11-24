# ТЗ Backend - Новости с пагинацией

## Модель News
```
id: number
title: string
image: string
published_date: string
views_count: number
short_description: string
categories: Category[]
```

## Модель Category
```
id: number
name: string
```

## API Endpoint

### GET /api/news

**Фильтры:**
- page (number)
- limit (number)
- search (string)
- category_id (number)
- published_date_start (string)
- published_date_end (string)
- top (boolean) - топовые новости

**Ответ:**
```json
{
  "data": [
    {
      "id": 1,
      "title": "Заголовок",
      "image": "url",
      "published_date": "2025-11-20",
      "views_count": 100,
      "short_description": "Описание",
      "categories": [{"id": 1, "name": "Категория"}]
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 95
  }
}
```

### GET /api/news/:id

**Ответ:**
```json
{
  "id": 1,
  "title": "Заголовок",
  "image": "url",
  "published_date": "2025-11-20",
  "views_count": 100,
  "short_description": "Краткое описание",
  "description": "<p>Полное описание в HTML</p>",
  "categories": [{"id": 1, "name": "Категория"}],
  "next_news_id": 2
}
```

---

## ОБЪЯВЛЕНИЯ

### Модель Announcement
```
id: number
user: {
  avatar: string
  username: string
}
title: string
image: string
created_at: string
```

### GET /api/announcements

**Фильтры:**
- page (number)
- limit (number)
- search (string)
- category_id (number)
- published_date_start (string)
- published_date_end (string)

---

## АНОНСЫ МЕРОПРИЯТИЙ

### Модель Event
```
id: number
image: string (url)
```

### GET /api/events

**Фильтры:**
- page (number)
- limit (number)
- search (string)
- category_id (number)

---

## ИНТЕРАКТИВНАЯ КАРТА

### GET /api/map/points

**Ответ:**
```json
{
  "data": [
    {
      "id": 1,
      "lat": 42.6977,
      "lng": 23.3219,
      "title": "Название точки",
      "type": "тип"
    }
  ]
}
```

---

## КАТАЛОГ ОРГАНИЗАЦИЙ

### Модель Organization
```
id: number
title: string
description: string
address: string
phone_number: string
lat: number
lng: number
```

### GET /api/organizations

**Ответ со списком организаций и координатами**

### GET /api/administrations

**Модель Administration:**
```
id: number
title: string
price: string (text)
grafik_raboty: string (text)
```

---

## ВАКАНСИИ

### Модель Vacancy
```
id: number
title: string
price: string (text)
grafik_raboty: string (text)
```

### GET /api/vacancies

**Ответ со списком вакансий**

### GET /api/vacancies/:id

**Ответ:**
```json
{
  "id": 1,
  "title": "Название вакансии",
  "price": "50000 руб",
  "grafik_raboty": "Полный день",
  "description": "<p>Описание в HTML</p>",
  "phone_number": "+7 123 456 7890",
  "email": "hr@example.com"
}
```

### POST /api/vacancies/apply

**Тело запроса:**
```json
{
  "vacancy_id": 1,
  "name": "Имя",
  "phone_number": "+7 123 456 7890",
  "message": "Сообщение"
}
```

---

## ИСТОРИЯ СЕЛА

### GET /api/village-history

**Список:**
```json
{
  "data": [
    {
      "id": 1,
      "title": "Название"
    }
  ]
}
```

### GET /api/village-history/:id

**Ответ:**
```json
{
  "id": 1,
  "title": "Название",
  "image": "url",
  "content": "<p>Контент в HTML</p>"
}
```

---

## ФОТОГАЛЕРЕЯ

### GET /api/photo-gallery

**Список:**
```json
{
  "data": [
    {
      "id": 1,
      "title": "Название альбома"
    }
  ]
}
```

### GET /api/photo-gallery/:id

**Ответ:**
```json
{
  "id": 1,
  "title": "Название альбома",
  "description": "Описание",
  "images": [
    {
      "id": 1,
      "url": "image_url",
      "thumbnail": "thumb_url"
    }
  ]
}
```

---

## ДОСТОПРИМЕЧАТЕЛЬНОСТИ

### GET /api/attractions

**Список:**
```json
{
  "data": [
    {
      "id": 1,
      "image": "url",
      "title": "Название",
      "short_description": "Краткое описание"
    }
  ]
}
```

### GET /api/attractions/:id

**Ответ:**
```json
{
  "id": 1,
  "title": "Название",
  "content": "<p>Полное описание</p>",
  "images": ["url1", "url2"],
  "coordinate": {
    "lat": 42.6977,
    "lng": 23.3219
  }
}
```

---

## GALLERY

### GET /api/gallery

**Список изображений:**
```json
{
  "data": [
    {
      "id": 1,
      "url": "image_url",
      "thumbnail": "thumb_url"
    }
  ]
}
```

---

## ОБРАТНАЯ СВЯЗЬ

### POST /api/feedback

**Тело запроса:**
```json
{
  "name": "Имя",
  "email": "email@example.com",
  "message": "Текст сообщения"
}
```

**Ответ:**
```json
{
  "success": true,
  "message": "Сообщение отправлено"
}
```

---

## Страницы
1. `/news` - список новостей
2. `/news/:id` - одна новость
3. `/categories` - список категорий
4. `/announcements` - объявления
5. `/events` - анонсы мероприятий
6. `/map` - интерактивная карта
7. `/organizations` - каталог организаций
8. `/vacancies` - вакансии
9. `/village-history` - история села
10. `/photo-gallery` - фотогалерея
11. `/attractions` - достопримечательности
12. `/gallery` - галерея изображений
13. `/contact` - обратная связь

## Требования
- Пагинация по page/limit
- Поиск по title и short_description
- Фильтр по category_id и датам
- Сортировка по дате (новые первые)
