from django.db import models


class Kittens(models.Model):
    url = models.CharField(max_length=200, unique=True)
    votes_up = models.PositiveIntegerField(default=0)
    votes_down = models.PositiveIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True)

    objects = KittensManager()

class KittensManager(models.Manager):
    
