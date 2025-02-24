from django.shortcuts import render
from .models import Anime, Manga
def index(request):
    return render(request, 'other/other.html')
def home(request):
    anime_list = Anime.objects.all().order_by('-rank')[:10]  # Топ 10 аниме
    manga_list = Manga.objects.all().order_by('-rank')[:10]  # Топ 10 манги
    return render(request, 'other/other.html', {'anime_list': anime_list, 'manga_list': manga_list})