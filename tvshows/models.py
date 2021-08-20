from django.db import models

# Create your models here.
#user name = himanchal
#password = qwerty@1Him


class Tvshow(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=50,default="")
    likes = models.IntegerField()
    active = models.BooleanField(default=True)
    trending = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img', default="")
    Hindi = models.BooleanField(default=False)
    English = models.BooleanField(default=False)
    trailer_link = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name


class Episode(models.Model):
    tv_id = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    season_no = models.IntegerField()
    pub_date = models.DateField()
    episode_no = models.IntegerField()
    episode_link = models.CharField(max_length=200)


    def __str__(self):
        return str(self.episode_no)