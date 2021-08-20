"""Moviesite URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('browse/', views.browse, name='browse'),
    path('browse/movie', views.browse_movie, name='browse_movie'),
    path('browse/tvshows', views.browse_tvshows, name='browse_tvshows'),
    path('how_to_download',views.download_process,name='download_process'),
    path('movie/', include('movies.urls')),
    path('movie<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('othersites/', views.othersite, name='othersites'),
    path('search/',views.search,name='search'),
    path('tvshow<int:tvshow_id>/', views.tvshow_detail, name='tvshow_detail'),
    path('tvshow<int:tvshow_id>/season<int:season_no>', views.tvshow_season_det, name='tvshow_season_det'),
    path('tvshow/', include('tvshows.urls')),
    # path('live/',  views.live, name='live'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
