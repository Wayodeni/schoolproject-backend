from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from articles.models import *


def articles_catalog(request):
    context = {}
    context['articles'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles-catalog.html', context)


def article(request, pk):
    # post = get_object_or_404(Post, pk=pk) - получает обьекты, или если такого обьекта с таким pk в бд нет, выдает 404.
    post = Post.objects.get(pk=pk)
    return render(request, 'article.html', {'post': post})

def books_catalog(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'books-catalog.html', {'books': books})
