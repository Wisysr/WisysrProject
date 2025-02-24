from django.contrib import admin
from .models import Anime, Manga

# Регистрируем модели в админке
admin.site.register(Anime)
admin.site.register(Manga)