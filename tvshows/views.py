from django.shortcuts import render
from .models import Tvshow
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def tvshow_by_name(request,slug):
    tvshows_list = [item for item in Tvshow.objects.all() if slug == item.name[0]]
    p = Paginator(tvshows_list,1)
    page_num = request.GET.get('page',1)

    try:
           page = p.page(page_num)
    except EmptyPage:
           page = p.page(1)

    act = {'tvshows_list':page,'slug':slug}
    return render(request,'tv_list.html',act)


def tvshow_byyear(request,tv_year):
    action = Tvshow.objects.filter(year=tv_year).order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(action, 12)
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    act = {'tvshows_list': content, 'cat': tv_year}
    return render(request, 'tv_list_year.html', act)

