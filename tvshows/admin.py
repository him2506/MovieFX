from django.contrib import admin
from .models import Tvshow,Episode
# Register your models here.

class TvshowAdmin(admin.ModelAdmin):
    list_display = ('name','year','active')


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('tv_id','season_no','episode_no')


admin.site.register(Tvshow,TvshowAdmin)

admin.site.register(Episode,EpisodeAdmin)