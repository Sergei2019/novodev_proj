from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TelegramUser
import hashlib
import hmac
import urllib.parse

User = get_user_model()

def verify_telegram_auth_data(auth_data):
    """
    Проверяет подлинность данных, полученных от Telegram Web App.
    auth_data: словарь с 'id', 'first_name', 'auth_date', 'hash'
    """
    bot_token = settings.TELEGRAM_BOT_TOKEN # Убедитесь, что токен бота в настройках
    data_check_arr = []
    for key, value in auth_data.items():
        if key != 'hash':
            data_check_arr.append(f"{key}={value}")
    data_check_arr.sort()
    data_check_string = '\n'.join(data_check_arr)

    secret_key = hashlib.sha256(bot_token.encode()).digest()
    hash_calculated = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    return hmac.compare_digest(hash_calculated, auth_data['hash'])

@api_view(['POST'])
@permission_classes([AllowAny])
def telegram_auth(request):
    """
    Аутентификация через Telegram Web App.
    Ожидает 'initData' в теле запроса.
    """
    init_data = request.data.get('initData')

    if not init_data:
        return Response({"error": "Init data is required"}, status=status.HTTP_400_BAD_REQUEST)

    parsed_data = dict(urllib.parse.parse_qsl(init_data))
    if 'hash' not in parsed_data:
        return Response({"error": "Hash is missing"}, status=status.HTTP_400_BAD_REQUEST)

    if not verify_telegram_auth_data(parsed_data):
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    telegram_id = int(parsed_data['id'])
    first_name = parsed_data.get('first_name', 'Unknown')
    last_name = parsed_data.get('last_name', '')
    username = parsed_data.get('username', '')
    email = parsed_data.get('email', '')

    # Проверяем, есть ли уже пользователь с таким Telegram ID
    try:
        tg_user = TelegramUser.objects.get(telegram_id=telegram_id)
        user = tg_user.user
    except TelegramUser.DoesNotExist:
        # Создаём нового пользователя Django
        # Логика создания может отличаться: username, email, ...
        username_for_django = username or f"tg_{telegram_id}"
        user = User.objects.create_user(
            username=username_for_django,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        TelegramUser.objects.create(user=user, telegram_id=telegram_id)

    # Выдаём JWT токены (аналогично Djoser)
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }, status=status.HTTP_200_OK)