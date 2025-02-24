from django.db import models

# Модель для аниме
class Anime(models.Model):
    objects = None
    title = models.CharField(max_length=100, verbose_name='Название аниме')
    rank = models.IntegerField(verbose_name='Рейтинг')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    release_year = models.IntegerField(verbose_name='Год выхода')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def str(self):
        return self.title

# Модель для манги
class Manga(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название манги')
    rank = models.IntegerField(verbose_name='Рейтинг')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def str(self):
        return self.title