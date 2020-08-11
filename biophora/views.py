from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from articles.models import *


def articles_catalog(request):
    context = {}
    context['articles'] = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles-catalog.html', context)


def article(request, pk):
    # post = get_object_or_404(Post, pk=pk) - получает обьекты, или если такого обьекта с таким pk в бд нет, выдает 404.
    article = Article.objects.get(pk=pk)
    return render(request, 'article.html', {'article': article})


def books_catalog(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'books-catalog.html', {'books': books})


def videos_catalog(request):
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'videos_catalog.html', {'videos': videos})


def recent(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:3]
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:3]
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:3]
    context = {}
    context['articles'] = articles
    context['books'] = books
    context['videos'] = videos
    return render(request, 'recent.html', context)

def about(request):
    return render(request, 'about.html')





