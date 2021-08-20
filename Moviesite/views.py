from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie,Websites
from movies.models import User
from tvshows.models import Tvshow
from tvshows.models import Episode
from django.db.models import Q
from ipware import get_client_ip


def index(request):
     trending_movie = Movie.objects.filter(trending=True)
     trending_tvshow = Tvshow.objects.filter(trending= True)

     ###### For IP Address
     def get_ip(request):
          ip, is_routable = get_client_ip(request)
          if ip is None:
               print("Unable to get the client's IP address")
          else:
               return ip
     ip = get_ip(request)
     u = User(user = ip)
     result = User.objects.filter(Q(user = ip))
     if len(result) == 1:
          print("User Exist")
          pass
     elif len(result)>1:
          print("User Exist more.....")
     else:
          u.save()
          print("User is Unique.")
     count = User.objects.all().count()
     param = {'trend': trending_movie, 'upcome': trending_tvshow,'count':count}
     return render(request, 'index.html', param)

def othersite(request):
     webpages = Websites.objects.all()
     return render(request, 'myhome.html',{'webpages':webpages})

def browse(request):
     return render(request, 'browse.html')

def browse_movie(request):
      return render(request, 'browsemovies.html')

def browse_tvshows(request):
     return render(request, 'browsetvshows.html')


def movie_detail(request,movie_id):
     movie = Movie.objects.filter(movie_id=movie_id)
     return render(request,'movie_detail.html',{'movie':movie[0]})

def tvshow_detail(request,tvshow_id):
     tvshow = Tvshow.objects.filter(id=tvshow_id)

     y= []
     for e in tvshow:
          for s in e.episode_set.all():
               y.append(s.season_no)

     list(set(y))
     return render(request,'tvshow_detail.html',{'tvshow':tvshow[0],'season':list(set(y))})


def tvshow_season_det(request,tvshow_id,season_no):
     episodes = Episode.objects.filter(tv_id=tvshow_id,season_no=season_no).order_by('episode_no')
     tvshow = Tvshow.objects.filter(id = tvshow_id)
     season_no = season_no
     return render(request,"tvshow_episodes.html",{'episodes':episodes,'season_no':season_no,'tvshow':tvshow[0]})

def search(request):
     qur = request.GET.get('search').lower()
     movie_list = [item for item in Movie.objects.all() if qur in item.movie_name.lower()]
     tv_list = [item for item in Tvshow.objects.all() if qur in item.name.lower()]
     # if len(tv_list) != 0:
     #      for item in tv_list:
     #           movie_list.append(item)
     # print(movie_list)
     return render(request,'search.html',{'movie_list':movie_list,'tv_list':tv_list,'qur':qur})


def download_process(request):
     return render(request,'how_to_down.html')

# def live(request):
#      return render(request,'Torrent_live.html')
