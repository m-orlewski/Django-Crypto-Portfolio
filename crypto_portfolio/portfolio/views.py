from django.shortcuts import render
from django.views.generic import ListView
import requests
# from django.http import HttpResponse

# Create your views here.

def home(request): 
    return render(request, 'portfolio/home.html')

def profile(request):
    raw_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return render(request, 'portfolio/portfolio.html', context={ 'coins': raw_data})

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About page'})
