from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from articles.models import Post


def articles_catalog(request):
    context = {}
    context['articles'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles-catalog.html', context)


def article(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'article.html', {'post': post})
