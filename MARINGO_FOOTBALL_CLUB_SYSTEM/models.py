from django.db import models

class Player(models.Model):
    idnumber = models.IntegerField(blank=False, null=False)
    fullname = models.CharField(max_length=30, blank=False, null=False)
    gender = models.EmailField(max_length=30, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    contact = models.IntegerField(blank=False, null=False)
    county = models.CharField(max_length=30, blank=False, null=False)
    school = models.CharField(max_length=30, blank=False, null=False)
    team = models.CharField(max_length=30, blank=False, null=False)
    photo = models.ImageField(max_length=30, blank=False, null=False)



def __str__(self):
    return self.name

