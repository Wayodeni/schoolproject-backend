from django.shortcuts import render
from django.utils import timezone
from articles.models import Post


def articles_catalog(request):
    context = {}

    context['articles'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles-catalog.html', context)
