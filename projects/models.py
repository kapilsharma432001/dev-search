from django.db import models
from django.db.models.base import Model
import uuid
from users.models import Profile

from django.db.models.deletion import CASCADE, SET_NULL

class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null = True, blank = True, default = 'default.jpg')
    demo_link = models.CharField(max_length = 2000, null=True, blank=True)
    source_link = models.CharField(max_length = 2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 

    def __str__(self):
        return self.title


class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # By null = True we are telling database that it could be NULL, by blank = True, we are telling the django that it could be NULL
    body = models.TextField(null=True, blank = True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 

    def __str__(self):
        return self.value



class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 

    def __str__(self):
        return self.name