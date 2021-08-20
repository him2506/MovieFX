from django.urls import path
from . import views

urlpatterns = [
    path("action/", views.actionmovie ,name = 'actionmovie'),
    path("adventure/", views.adventuremovie ,name = 'adventuremovie'),
    path("animation/", views.animationmovie ,name = 'animationmovie'),
    path("comedy/", views.comedymovie ,name = 'comedynmovie'),
    path("documentry/", views.documentrymovie ,name = 'documentrymovie'),
    path("crime/", views.crimemovie ,name = 'crimemovie'),
    path("drama/", views.dramamovie ,name = 'dramamovie'),
    path("family/", views.familymovie ,name = 'familymovie'),
    path("fantasy/", views.fantasymovie ,name = 'fantasymovie'),
    path("horror/", views.horrormovie ,name = 'horrormovie'),
    path("history/", views.historymovie ,name = 'historymovie'),
    path("musical/", views.musicalmovie ,name = 'musicalmovie'),
    path("mystery/", views.mysterymovie ,name = 'mysterymovie'),
    path("sci_fi/", views.sci_fimovie ,name = 'sci_fimovie'),
    path("sport/", views.sportmovie ,name = 'sportmovie'),
    path("thriller/", views.thrillermovie ,name = 'thrillermovie'),
    path("war/", views.warmovie ,name = 'warmovie'),

    path('<int:movie_year>/',views.searchbyyear,name='searchbyyear'),

]
