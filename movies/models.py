from django.db import models

# Create your models here.
#user name = himanchal
#password = qwerty@1Him


class Movie(models.Model):
    movie_id = models.AutoField(primary_key = True)
    movie_name = models.CharField(max_length=200)
    year = models.CharField(max_length=50,default="")
    likes = models.CharField(max_length=50,default="")
    active = models.BooleanField(default=True)

    # desc = models.CharField(max_length=1000)
    # upload_to me img wo folder h jahan images upload hongi.
    image = models.ImageField(upload_to='img', default="")
    magnet_link_720p = models.CharField(max_length=1000,default="")
    magnet_link_1080p = models.CharField(max_length=1000,default="")
    trailer_link = models.CharField(max_length=1000,default="")

    trending = models.BooleanField(default=False)
    

    Hindi = models.BooleanField(default=False)
    English = models.BooleanField(default=False)
   
    action = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)
    comedy = models.BooleanField(default=False)
    crime = models.BooleanField(default=False)
    documentry = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    fantasy = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    horror = models.BooleanField(default=False)
    musical = models.BooleanField(default=False)
    mystery = models.BooleanField(default=False)
    sci_fi = models.BooleanField(default=False)
    sport = models.BooleanField(default=False)
    thriller = models.BooleanField(default=False)
    war = models.BooleanField(default=False)


    def __str__(self):
        return self.movie_name


class User(models.Model):
    user = models.TextField(default=None)
    def __str__(self):
        return self.user



class Websites(models.Model):
    webname = models.CharField(max_length=200)
    weblink = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.webname