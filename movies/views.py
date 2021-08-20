from django.shortcuts import render
from django.http import Http404
from .models import Movie
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def searchbyyear(request,movie_year):
     action = Movie.objects.filter(year=movie_year).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     act = {'action': content, 'cat': movie_year}
     return render(request,'movie_list.html',act)


def actionmovie(request):
     action = Movie.objects.filter(action = True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Action'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def adventuremovie(request):
     action = Movie.objects.filter(adventure=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Adventure'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def animationmovie(request):
     action = Movie.objects.filter(animation=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Animation'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def comedymovie(request):
     action = Movie.objects.filter(comedy=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Comedy'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def crimemovie(request):
     action = Movie.objects.filter(crime=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Crime'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def documentrymovie(request):
     action = Movie.objects.filter(documentry=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Documentry'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def dramamovie(request):
     action = Movie.objects.filter(drama=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Drama'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def familymovie(request):
     action = Movie.objects.filter(family=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Family'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def fantasymovie(request):
     action = Movie.objects.filter(fantasy=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Fantasy'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def horrormovie(request):
     action = Movie.objects.filter(horror=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Horror'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def historymovie(request):
     action = Movie.objects.filter(history=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'History'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def musicalmovie(request):
     action = Movie.objects.filter(musical=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Musical'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def mysterymovie(request):
     action = Movie.objects.filter(mystery=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Mystery'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def sci_fimovie(request):
     action = Movie.objects.filter(sci_fi=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Sci-fi'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def sportmovie(request):
     action = Movie.objects.filter(sport=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Sport'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def thrillermovie(request):
     action = Movie.objects.filter(thriller=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'Thriller'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

def warmovie(request):
     action = Movie.objects.filter(war=True).order_by('movie_id')
     page = request.GET.get('page', 1)
     paginator = Paginator(action, 12)
     try:
          content = paginator.page(page)
     except PageNotAnInteger:
          content = paginator.page(1)
     except EmptyPage:
          content = paginator.page(paginator.num_pages)
     cat = 'War'
     return render(request, 'movie_list.html',{'action':content,'cat': cat})

