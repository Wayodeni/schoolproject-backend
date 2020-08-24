"""schoolproject_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static #обязательно для того чтобы картика виднелась
from django.urls import path
from articles import views
from schoolproject_backend import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles_catalog/', views.articles_catalog, name='articles_catalog'),
    path('article/<int:pk>/', views.article, name='article'),
    path('books_catalog/', views.books_catalog, name='books_catalog'),
    path('videos_catalog/', views.videos_catalog, name='videos_catalog'),
    path('', views.recent, name='recent'),
    path('about/', views.about, name='about'),
    path('search_results/', views.search_results, name='search_results')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #обязательно для того чтобы картика виднелась


