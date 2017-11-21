from django.db import models
import datetime

# Create your models here.

class Scholar(models.Model):
    GENDER_CHOICE = {
        (0, 'Male'),
        (1, 'Female')
    }

    guid = models.CharField(max_length = 50, db_index = True, unique = True, null = True)
    classification = models.CharField(max_length = 30, blank = True, null = True)
    name = models.CharField(max_length = 100, null = True)
    sex = models.IntegerField(choices = GENDER_CHOICE, null = True)
    birthday = models.DateTimeField(null = True)
    degree = models.CharField(max_length = 1, null = True)
    title = models.CharField(max_length = 1, null = True)
    graduateschool = models.CharField(max_length = 50, null = True)
    subject = models.CharField(max_length = 50, null = True)
    introduction = models.TextField(blank = True, null = True)
    achievement = models.TextField(blank = True, null = True)
    affiliation = models.TextField(blank = True, null = True)
    nationality = models.CharField(max_length = 30, null = True)
    email = models.CharField(max_length = 50, null = True)
    homepage = models.TextField(null = True)
    photourl = models.TextField(null = True)
    lastmodified = models.DateTimeField(null = True)
    keywords = models.TextField(null = True)
    position = models.CharField(max_length = 50, null = True)
    rank = models.IntegerField(null = True)
