from django.db import models
from django.utils import timezone

class Account(models.Model):
    login = models.CharField(max_length=100, unique=True)
    email = models.EmailField(default = 'from@example.com',unique=True)
    password = models.CharField(max_length=100)
    value = models.FloatField()
    date_of_joining = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.login + " - wartosc portfela: " + self.value