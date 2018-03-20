from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='HEADER.jpg',blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    GOLD_MAKING ="Gold making"
    DUNGEONS = "Dungeons"
    FRACTALS = "Fractals"
    RAIDS = "Raids"
    BUILDS = "Builds"
    theme_choices = (
        (GOLD_MAKING,"Gold making"),
        (DUNGEONS,"Dungeons"),
        (FRACTALS,"Fractals"),
        (RAIDS,"Raids"),
        (BUILDS,"Builds")
    )
    theme = models.CharField(max_length= 20, choices = theme_choices, default =BUILDS)
    #add author,thumbnail, lasteditor
    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:100] + '...'

    def deactivate(self):
        self.active = False
