from django.contrib import admin
from .models import Movie,User,Websites

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name','movie_id','trending','active','year')


admin.site.register(Movie,MovieAdmin)
admin.site.register(User)
admin.site.register(Websites)



