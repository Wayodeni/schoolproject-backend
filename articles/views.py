from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from articles.models import *
from django.db.models import Q

def articles_catalog(request):
    context = {}
    context['articles'] = Article.objects.order_by('-published_date')
    return render(request, 'articles-catalog.html', context)


def article(request, pk):
    # post = get_object_or_404(Post, pk=pk) - получает обьекты, или если такого обьекта с таким pk в бд нет, выдает 404.
    article = Article.objects.get(pk=pk)
    return render(request, 'article.html', {'article': article})


def books_catalog(request):
    books = Book.objects.order_by('-published_date')
    return render(request, 'books-catalog.html', {'books': books})


def videos_catalog(request):
    videos = Video.objects.order_by('-published_date')
    return render(request, 'videos_catalog.html', {'videos': videos})


def recent(request):
    articles = Article.objects.order_by('-published_date')[:3]
    books = Book.objects.order_by('-published_date')[:3]
    videos = Video.objects.order_by('-published_date')[:3]
    context = {}
    context['articles'] = articles
    context['books'] = books
    context['videos'] = videos
    return render(request, 'recent.html', context)


def about(request):
    return render(request, 'about.html')


def search_results(request):
    search_query = request.GET.get('search', '')

    if search_query:
        articles = Article.objects.filter(title__icontains=search_query)
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        videos = Video.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

        context = {}
        context['articles'] = articles
        context['books'] = books
        context['videos'] = videos

        return render(request, 'search-results.html', context)
    else:
        return render(request, 'search-results.html')
