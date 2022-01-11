from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Asset(models.Model):
    coin_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateTimeField()
    price = models.FloatField()
    portfolio = models.ForeignKey("Portfolio", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}({self.name}): Amount: {self.amount}, Price: {self.price}, Date: {self.date}'
