from django.urls import path
from . import views

urlpatterns = [
    path("<slug>/", views.tvshow_by_name ,name = 'tvshow_by_name'),
    path('year/<int:tv_year>/', views.tvshow_byyear, name='tvshow_byyear'),
]