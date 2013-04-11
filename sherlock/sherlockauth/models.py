from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

class SherlockUser(User.model):
    photo = models.ImageField(upload_to='userphotos')

    #user profile info (main)
    race = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    
    #user profile info (possiblez) some info that might be fun to play around with in the future
    mood = models.CharField(max_length=1024, null=True) #not sure how I want to store this one yet. word descriptions? numerical levels? idk
    occupation = models.CharField(max_length=1024, null=True) #this one might actually be kind of fun
    intelligence = models.CharField(max_length=1024, null=True) #not sure how to measure this either. degree of education?
    socialclass = models.CharField(max_length=1024, null=True) #income levels?
    attractiveness = models.IntegerField(null=True) #1-10 i guess
