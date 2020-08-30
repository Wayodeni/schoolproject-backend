from django.conf import settings
from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = HTMLField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Book(models.Model):
    preview = models.ImageField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    download_link = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Video(models.Model):
    preview = models.ImageField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    watch_link = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
